# app/tts.py
import logging
import json
import edge_tts
from io import BytesIO
from pydub import AudioSegment
import re
from datetime import timedelta
from typing import List
import redis.asyncio as redis

logger = logging.getLogger(__name__)


class TTSManager:
    def __init__(self, session_id: str, redis_client: redis.Redis, expiry_minutes: int = 5):
        self.session_id = session_id
        self.redis = redis_client
        self.expiry = timedelta(minutes=expiry_minutes)

    def _get_chunk_key(self, index: int) -> str:
        return f"tts:{self.session_id}:chunk:{index}"

    def _get_metadata_key(self) -> str:
        return f"tts:{self.session_id}:metadata"

    def _split_text(self, text: str, max_length: int = 300) -> List[str]:
        """Split text into smaller chunks"""
        sentences = re.split('[.!?؟]', text)
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            if len(current_chunk) + len(sentence) <= max_length:
                current_chunk += sentence + ". "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + ". "

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    async def _generate_audio_chunk(self, text: str, voice: str, speed: float) -> bytes:
        """Generate audio for a single chunk of text"""
        try:
            output_buffer = BytesIO()
            communicate = edge_tts.Communicate(
                text=text,
                voice=voice,
                rate=f"{speed:+.0f}%"
            )
            await communicate.save(output_buffer)
            output_buffer.seek(0)  # Reset buffer pointer to start
            raw_data = output_buffer.getvalue()
            output_buffer.close()  # Cleanup
            return raw_data
        except Exception as e:
            logger.error(f"Error generating audio: {e}")
            raise

    async def _merge_audio_chunks(self) -> bytes:
        """Merge all audio chunks"""
        try:
            metadata = json.loads(await self.redis.get(self._get_metadata_key()))
            combined = AudioSegment.empty()

            for i in range(metadata["total_chunks"]):
                chunk_data = await self.redis.get(self._get_chunk_key(i))
                if not chunk_data:
                    raise ValueError(f"Chunk {i} not found")

                chunk_buffer = BytesIO(chunk_data)
                chunk_buffer.seek(0)
                audio_chunk = AudioSegment.from_file(chunk_buffer, format="mp3")
                chunk_buffer.close()  # Cleanup
                combined += audio_chunk

            output_buffer = BytesIO()
            combined.export(output_buffer, format="mp3")
            output_buffer.seek(0)
            final_data = output_buffer.getvalue()
            output_buffer.close()  # Cleanup
            return final_data

        except Exception as e:
            logger.error(f"Error merging audio chunks: {e}")
            raise

    async def process_text(self, text: str, voice: str, speed: float = 1.0) -> bytes:
        """Process text and convert to audio"""
        try:
            chunks = self._split_text(text)

            metadata = {
                "total_chunks": len(chunks),
                "voice": voice,
                "speed": speed,
                "status": "processing"
            }

            await self.redis.set(
                self._get_metadata_key(),
                json.dumps(metadata),
                ex=int(self.expiry.total_seconds())
            )

            for i, chunk in enumerate(chunks):
                audio_data = await self._generate_audio_chunk(chunk, voice, speed)
                chunk_key = self._get_chunk_key(i)
                await self.redis.set(
                    chunk_key,
                    audio_data,
                    ex=int(self.expiry.total_seconds())
                )

            final_audio = await self._merge_audio_chunks()

            metadata["status"] = "completed"
            await self.redis.set(
                self._get_metadata_key(),
                json.dumps(metadata),
                ex=int(self.expiry.total_seconds())
            )

            return final_audio

        except Exception as e:
            logger.error(f"Error processing text: {e}")
            raise

    async def cleanup(self):
        """Clean up all session data"""
        try:
            metadata_str = await self.redis.get(self._get_metadata_key())
            if metadata_str:
                metadata = json.loads(metadata_str)
                for i in range(metadata.get("total_chunks", 0)):
                    await self.redis.delete(self._get_chunk_key(i))
            await self.redis.delete(self._get_metadata_key())
            logger.info(f"Cleaned up session: {self.session_id}")
        except Exception as e:
            logger.error(f"Error cleaning up: {e}")