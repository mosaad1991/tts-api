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
            # الأصوات العربية من مختلف الدول
            "ar-DZ-AminaNeural": {
                "name": "أمينة",
                "gender": "female",
                "dialect": "algerian"
            },
            "ar-BH-LailaNeural": {
                "name": "ليلى",
                "gender": "female",
                "dialect": "bahraini"
            },
            "ar-EG-SalmaNeural": {
                "name": "سلمى",
                "gender": "female",
                "dialect": "egyptian"
            },
            "ar-IQ-RanaNeural": {
                "name": "رنا",
                "gender": "female",
                "dialect": "iraqi"
            },
            "ar-JO-SanaNeural": {
                "name": "سناء",
                "gender": "female",
                "dialect": "jordanian"
            },
            "ar-KW-NouraNeural": {
                "name": "نورة",
                "gender": "female",
                "dialect": "kuwaiti"
            },
            "ar-LB-LaylaNeural": {
                "name": "ليلى",
                "gender": "female",
                "dialect": "lebanese"
            },
            "ar-LY-ImanNeural": {
                "name": "إيمان",
                "gender": "female",
                "dialect": "libyan"
            },
            "ar-MA-MounaNeural": {
                "name": "مونى",
                "gender": "female",
                "dialect": "moroccan"
            },
            "ar-OM-AyshaNeural": {
                "name": "عائشة",
                "gender": "female",
                "dialect": "omani"
            },
            "ar-QA-AmalNeural": {
                "name": "آمال",
                "gender": "female",
                "dialect": "qatari"
            },
            "ar-SA-ZariyahNeural": {
                "name": "زريا",
                "gender": "female",
                "dialect": "saudi"
            },
            "ar-SY-AmanyNeural": {
                "name": "أماني",
                "gender": "female",
                "dialect": "syrian"
            },
            "ar-TN-ReemNeural": {
                "name": "ريم",
                "gender": "female",
                "dialect": "tunisian"
            },
            "ar-AE-FatimaNeural": {
                "name": "فاطمة",
                "gender": "female",
                "dialect": "emirati"
            },
            "ar-YE-MaryamNeural": {
                "name": "مريم",
                "gender": "female",
                "dialect": "yemeni"
            }
        },
        "en": {
            # الأصوات الإنجليزية من مختلف البلدان
            "en-AU-NatashaNeural": {
                "name": "Natasha",
                "gender": "female",
                "dialect": "australian"
            },
            "en-CA-ClaraNeural": {
                "name": "Clara",
                "gender": "female",
                "dialect": "canadian"
            },
            "en-HK-YanNeural": {
                "name": "Yan",
                "gender": "female",
                "dialect": "hong kong"
            },
            "en-IN-NeerjaNeural": {
                "name": "Neerja",
                "gender": "female",
                "dialect": "indian"
            },
            "en-IE-EmilyNeural": {
                "name": "Emily",
                "gender": "female",
                "dialect": "irish"
            },
            "en-KE-AsiliaNeural": {
                "name": "Asilia",
                "gender": "female",
                "dialect": "kenyan"
            },
            "en-NZ-MollyNeural": {
                "name": "Molly",
                "gender": "female",
                "dialect": "new zealand"
            },
            "en-NG-EzinneNeural": {
                "name": "Ezinne",
                "gender": "female",
                "dialect": "nigerian"
            },
            "en-PH-RosaNeural": {
                "name": "Rosa",
                "gender": "female",
                "dialect": "philippine"
            },
            "en-SG-LunaNeural": {
                "name": "Luna",
                "gender": "female",
                "dialect": "singapore"
            },
            "en-ZA-LeahNeural": {
                "name": "Leah",
                "gender": "female",
                "dialect": "south african"
            },
            "en-GB-LibbyNeural": {
                "name": "Libby",
                "gender": "female",
                "dialect": "british"
            },
            "en-US-AvaNeural": {
                "name": "Ava",
                "gender": "female",
                "dialect": "american"
            }
        }
    }

settings = Settings()