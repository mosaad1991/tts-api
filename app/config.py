# app/config.py
import os
from typing import List

class Settings:
    REDIS_URLS: List[str] = [
        os.getenv("REDIS_MERNA_URL", ""),
        os.getenv("REDIS_AQRABENO_URL", ""),
        os.getenv("REDIS_SWALF_URL", ""),
        os.getenv("REDIS_MOSAAD_URL", "")
    ]
    
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://serene-travesseiro-3ad48c.netlify.app/"
    ]
    
    SUPPORTED_VOICES = {
        "ar": {
            "ar-EG-ShakirNeural": {
                "name": "شاكر",
                "gender": "male",
                "dialect": "egyptian"
            },
            "ar-SA-HamedNeural": {
                "name": "حامد",
                "gender": "male",
                "dialect": "gulf"
            }
        },
        "en": {
            "en-US-AriaNeural": {
                "name": "Aria",
                "gender": "female",
                "dialect": "american"
            },
            "en-GB-RyanNeural": {
                "name": "Ryan",
                "gender": "male",
                "dialect": "british"
            }
        }
    }

settings = Settings()