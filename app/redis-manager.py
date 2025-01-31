# app/redis_manager.py
import asyncio
import logging
from datetime import datetime, timedelta
from .utils import get_random_redis

logger = logging.getLogger(__name__)


class RedisCleanupManager:
    def __init__(self, cleanup_interval: int = 300, max_storage_time: int = 600):
        self.cleanup_interval = cleanup_interval
        self.max_storage_time = max_storage_time
        self.is_running = False

    async def start_cleanup_task(self):
        self.is_running = True
        while self.is_running:
            try:
                await self.cleanup_expired_data()
                await asyncio.sleep(self.cleanup_interval)
            except Exception as e:
                logger.error(f"Cleanup error: {e}")
                await asyncio.sleep(60)

    async def cleanup_expired_data(self):
        redis_client = await get_random_redis()
        try:
            cursor = 0
            while True:
                cursor, keys = await redis_client.scan(cursor, match="tts:*")
                for key in keys:
                    try:
                        ttl = await redis_client.ttl(key)
                        if ttl <= 0:
                            await redis_client.delete(key)
                            logger.info(f"Deleted expired key: {key}")
                    except Exception as e:
                        logger.error(f"Error processing key {key}: {e}")

                if cursor == 0:
                    break

            logger.info("Cleanup completed successfully")
        except Exception as e:
            logger.error(f"Redis cleanup failed: {e}")
        finally:
            await redis_client.close()

    async def stop(self):
        self.is_running = False