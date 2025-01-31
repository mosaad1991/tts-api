# app/utils.py
import redis.asyncio as redis
import random
from typing import Any
from .config import settings

async def get_random_redis() -> redis.Redis:
    """Get a random Redis connection from the pool"""
    url = random.choice(settings.REDIS_URLS)
    if not url:
        raise ValueError("No Redis URLs configured")
    return await redis.from_url(url)

def validate_voice(language: str, voice_id: str) -> bool:
    """Validate if voice exists for language"""
    return (
        language in settings.SUPPORTED_VOICES and 
        voice_id in settings.SUPPORTED_VOICES[language]
    )