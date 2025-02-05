# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional
import logging
import asyncio
import os

from .config import settings
from .tts import TTSManager
from .utils import get_random_redis, validate_voice
from .redis_manager import RedisCleanupManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Text to Speech API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "api_version": "1.0",
        "endpoints": {
            "health": "/health",
            "voices": "/voices/{language}",
            "tts": "/tts"
        }
    }

# Initialize Redis Cleanup Manager
cleanup_manager = RedisCleanupManager(
    cleanup_interval=int(os.getenv("CLEANUP_INTERVAL", 300)),
    max_storage_time=int(os.getenv("MAX_STORAGE_TIME", 600))
)

class TTSRequest(BaseModel):
    text: str
    language: str
    voice: str
    speed: Optional[float] = 1.0

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(cleanup_manager.start_cleanup_task())

@app.on_event("shutdown")
async def shutdown_event():
    await cleanup_manager.stop()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/voices/{language}")
async def get_voices(language: str):
    if language not in settings.SUPPORTED_VOICES:
        raise HTTPException(status_code=400, detail="Unsupported language")
    return settings.SUPPORTED_VOICES[language]

@app.options("/tts")
async def options_tts():
    return {}

@app.options("/voices/{language}")
async def options_voices():
    return {}

@app.post("/tts")
async def text_to_speech(request: TTSRequest):
    try:
        if not validate_voice(request.language, request.voice):
            raise HTTPException(status_code=400, detail="Invalid language or voice combination")
        
        redis_client = await get_random_redis()
        session_id = f"tts_{id(request)}_{asyncio.current_task().get_name()}"
        
        tts_manager = TTSManager(
            session_id=session_id,
            redis_client=redis_client
        )
        
        audio_data = await tts_manager.process_text(
            text=request.text,
            voice=request.voice,
            speed=request.speed
        )
        
        await tts_manager.cleanup()
        await redis_client.close()
        
        return Response(
            content=audio_data,
            media_type="audio/mpeg",
            headers={"Content-Disposition": "attachment; filename=tts_output.mp3"}
        )
        
    except Exception as e:
        logger.error(f"Error processing TTS request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))