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
        # الأصوات الذكورية
        "ar-DZ-IsmaelNeural": {
            "name": "إسماعيل",
            "gender": "male",
            "dialect": "جزائري"
        },
        "ar-BH-AliNeural": {
            "name": "علي",
            "gender": "male", 
            "dialect": "بحريني"
        },
        "ar-EG-ShakirNeural": {
            "name": "شاكر",
            "gender": "male", 
            "dialect": "مصري"
        },
        "ar-IQ-BasselNeural": {
            "name": "باسل",
            "gender": "male",
            "dialect": "عراقي"
        },
        "ar-JO-TaimNeural": {
            "name": "تيم",
            "gender": "male",
            "dialect": "أردني"
        },
        "ar-KW-FahedNeural": {
            "name": "فهد",
            "gender": "male",
            "dialect": "كويتي"
        },
        "ar-LB-RamiNeural": {
            "name": "رامي",
            "gender": "male",
            "dialect": "لبناني"
        },
        "ar-LY-OmarNeural": {
            "name": "عمر",
            "gender": "male",
            "dialect": "ليبي"
        },
        "ar-MA-JamalNeural": {
            "name": "جمال",
            "gender": "male",
            "dialect": "مغربي"
        },
        "ar-OM-AbdullahNeural": {
            "name": "عبدالله",
            "gender": "male",
            "dialect": "عماني"
        },
        "ar-QA-MoazNeural": {
            "name": "معاذ",
            "gender": "male",
            "dialect": "قطري"
        },
        "ar-SA-HamedNeural": {
            "name": "حامد",
            "gender": "male",
            "dialect": "سعودي"
        },
        "ar-SY-LaithNeural": {
            "name": "ليث",
            "gender": "male",
            "dialect": "سوري"
        },
        "ar-TN-HediNeural": {
            "name": "هادي",
            "gender": "male",
            "dialect": "تونسي"
        },
        "ar-AE-HamdanNeural": {
            "name": "حمدان",
            "gender": "male",
            "dialect": "إماراتي"
        },
        "ar-YE-SalehNeural": {
            "name": "صالح",
            "gender": "male",
            "dialect": "يمني"
        },

        # الأصوات الأنثوية (المضافة سابقًا)
        "ar-DZ-AminaNeural": {
            "name": "أمينة", 
            "gender": "female",
            "dialect": "جزائري"
        },
        "ar-BH-LailaNeural": {
            "name": "ليلى",
            "gender": "female", 
            "dialect": "بحريني"
        },
        "ar-EG-SalmaNeural": {
            "name": "سلمى",
            "gender": "female", 
            "dialect": "مصري"
        },
        "ar-IQ-RanaNeural": {
            "name": "رنا",
            "gender": "female",
            "dialect": "عراقي"
        },
        "ar-JO-SanaNeural": {
            "name": "سناء",
            "gender": "female", 
            "dialect": "أردني"
        },
        "ar-KW-NouraNeural": {
            "name": "نورة",
            "gender": "female",
            "dialect": "كويتي"
        },
        "ar-LB-LaylaNeural": {
            "name": "ليلى",
            "gender": "female", 
            "dialect": "لبناني"
        },
        "ar-LY-ImanNeural": {
            "name": "إيمان",
            "gender": "female", 
            "dialect": "ليبي"
        },
        "ar-MA-MounaNeural": {
            "name": "مونى",
            "gender": "female", 
            "dialect": "مغربي"
        },
        "ar-OM-AyshaNeural": {
            "name": "عائشة",
            "gender": "female", 
            "dialect": "عماني"
        },
        "ar-QA-AmalNeural": {
            "name": "آمال",
            "gender": "female",
            "dialect": "قطري"
        },
        "ar-SA-ZariyahNeural": {
            "name": "زريا",
            "gender": "female", 
            "dialect": "سعودي"
        },
        "ar-SY-AmanyNeural": {
            "name": "أماني",
            "gender": "female", 
            "dialect": "سوري"
        },
        "ar-TN-ReemNeural": {
            "name": "ريم",
            "gender": "female", 
            "dialect": "تونسي"
        },
        "ar-AE-FatimaNeural": {
            "name": "فاطمة",
            "gender": "female", 
            "dialect": "إماراتي"
        },
        "ar-YE-MaryamNeural": {
            "name": "مريم",
            "gender": "female", 
            "dialect": "يمني"
        }
    },
        "en": {
    # الأصوات الإنجليزية القديمة
    "en-AU-NatashaNeural": {
        "name": "Natasha",
        "gender": "female",
        "dialect": "أسترالي"
    },
    "en-AU-WilliamNeural": {
        "name": "William",
        "gender": "male",
        "dialect": "أسترالي"
    },
    "en-CA-ClaraNeural": {
        "name": "Clara",
        "gender": "female",
        "dialect": "كندي"
    },
    "en-CA-LiamNeural": {
        "name": "Liam",
        "gender": "male",
        "dialect": "كندي"
    },
    "en-HK-SamNeural": {
        "name": "Sam",
        "gender": "male",
        "dialect": "هونغ كونغ"
    },
    "en-HK-YanNeural": {
        "name": "Yan",
        "gender": "female",
        "dialect": "هونغ كونغ"
    },
    "en-IN-NeerjaExpressiveNeural": {
        "name": "Neerja (Expressive)",
        "gender": "female",
        "dialect": "هندي"
    },
    "en-IN-NeerjaNeural": {
        "name": "Neerja",
        "gender": "female",
        "dialect": "هندي"
    },
    "en-IN-PrabhatNeural": {
        "name": "Prabhat",
        "gender": "male",
        "dialect": "هندي"
    },
    "en-IE-ConnorNeural": {
        "name": "Connor",
        "gender": "male",
        "dialect": "أيرلندي"
    },
    "en-IE-EmilyNeural": {
        "name": "Emily",
        "gender": "female",
        "dialect": "أيرلندي"
    },
    "en-KE-AsiliaNeural": {
        "name": "Asilia",
        "gender": "female",
        "dialect": "كيني"
    },
    "en-KE-ChilembaNeural": {
        "name": "Chilemba",
        "gender": "male",
        "dialect": "كيني"
    },
    "en-NZ-MitchellNeural": {
        "name": "Mitchell",
        "gender": "male",
        "dialect": "نيوزيلندي"
    },
    "en-NZ-MollyNeural": {
        "name": "Molly",
        "gender": "female",
        "dialect": "نيوزيلندي"
    },
    "en-NG-AbeoNeural": {
        "name": "Abeo",
        "gender": "male",
        "dialect": "نيجيري"
    },
    "en-NG-EzinneNeural": {
        "name": "Ezinne",
        "gender": "female",
        "dialect": "نيجيري"
    },
    "en-PH-JamesNeural": {
        "name": "James",
        "gender": "male",
        "dialect": "فلبيني"
    },
    "en-PH-RosaNeural": {
        "name": "Rosa",
        "gender": "female",
        "dialect": "فلبيني"
    },
    "en-SG-LunaNeural": {
        "name": "Luna",
        "gender": "female",
        "dialect": "سنغافوري"
    },
    "en-SG-WayneNeural": {
        "name": "Wayne",
        "gender": "male",
        "dialect": "سنغافوري"
    },
    "en-ZA-LeahNeural": {
        "name": "Leah",
        "gender": "female",
        "dialect": "جنوب أفريقي"
    },
    "en-ZA-LukeNeural": {
        "name": "Luke",
        "gender": "male",
        "dialect": "جنوب أفريقي"
    },
    "en-TZ-ElimuNeural": {
        "name": "Elimu",
        "gender": "male",
        "dialect": "تنزاني"
    },
    "en-TZ-ImaniNeural": {
        "name": "Imani",
        "gender": "female",
        "dialect": "تنزاني"
    },
    "en-GB-LibbyNeural": {
        "name": "Libby",
        "gender": "female",
        "dialect": "بريطاني"
    },
    "en-GB-MaisieNeural": {
        "name": "Maisie",
        "gender": "female",
        "dialect": "بريطاني"
    },
    "en-GB-RyanNeural": {
        "name": "Ryan",
        "gender": "male",
        "dialect": "بريطاني"
    },
    "en-GB-SoniaNeural": {
        "name": "Sonia",
        "gender": "female",
        "dialect": "بريطاني"
    },
    "en-GB-ThomasNeural": {
        "name": "Thomas",
        "gender": "male",
        "dialect": "بريطاني"
    },
    "en-US-AvaMultilingualNeural": {
        "name": "Ava (Multilingual)",
        "gender": "female",
        "dialect": "أمريكي متعدد اللغات"
    },
    "en-US-AndrewMultilingualNeural": {
        "name": "Andrew (Multilingual)",
        "gender": "male",
        "dialect": "أمريكي متعدد اللغات"
    },
    "en-US-EmmaMultilingualNeural": {
        "name": "Emma (Multilingual)",
        "gender": "female",
        "dialect": "أمريكي متعدد اللغات"
    },
    "en-US-BrianMultilingualNeural": {
        "name": "Brian (Multilingual)",
        "gender": "male",
        "dialect": "أمريكي متعدد اللغات"
    },
    "en-US-AvaNeural": {
        "name": "Ava",
        "gender": "female",
        "dialect": "أمريكي"
    },
    "en-US-AndrewNeural": {
        "name": "Andrew",
        "gender": "male",
        "dialect": "أمريكي"
    },
    "en-US-EmmaNeural": {
        "name": "Emma",
        "gender": "female",
        "dialect": "أمريكي"
    },
    "en-US-BrianNeural": {
        "name": "Brian",
        "gender": "male",
        "dialect": "أمريكي"
    },
    "en-US-AnaNeural": {
        "name": "Ana",
        "gender": "female",
        "dialect": "أمريكي"
    },
    "en-US-AriaNeural": {
        "name": "Aria",
        "gender": "female",
        "dialect": "أمريكي"
    },
    "en-US-ChristopherNeural": {
        "name": "Christopher",
        "gender": "male",
        "dialect": "أمريكي"
    },
    "en-US-EricNeural": {
        "name": "Eric",
        "gender": "male",
        "dialect": "أمريكي"
    },
    "en-US-GuyNeural": {
        "name": "Guy",
        "gender": "male",
        "dialect": "أمريكي"
    },
    "en-US-JennyNeural": {
        "name": "Jenny",
        "gender": "female",
        "dialect": "أمريكي"
    },
    "en-US-MichelleNeural": {
        "name": "Michelle",
        "gender": "female",
        "dialect": "أمريكي"
    },
    "en-US-RogerNeural": {
        "name": "Roger",
        "gender": "male",
        "dialect": "أمريكي"
    },
    "en-US-SteffanNeural": {
        "name": "Steffan",
        "gender": "male",
        "dialect": "أمريكي"
    }
}

settings = Settings()