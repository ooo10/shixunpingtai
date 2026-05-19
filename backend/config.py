import os
from dotenv import load_dotenv

load_dotenv()

ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "9bbac3df405e4f31bbab3bb2be5427d5.NzKAbUMTNxwwUp0H")
ZHIPU_API_BASE = "https://open.bigmodel.cn/api/paas/v4"

RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY", "")
RUNWAY_API_BASE = "https://api.dev.runwayml.com/v1"

TENCENT_API_KEY = os.getenv("TENCENT_API_KEY", "sk-ZGQgA4htjkfXhHjXEQiMvuiz2fh6PvzmXEDuUPFn3nM9VBV2")

API_CONFIG = {
    "text": {
        "model": "glm-5.1",
        "temperature": 0.7,
        "max_tokens": 2000
    },
    "image": {
        "model": "glm-image",
        "size": "1280x1280",
        "quality": "hd"
    },
    "video": {
        "model": "HY-Video-1.5",
        "duration": 5,
        "ratio": "16:9"
    },
    "audio": {
        "model": "glm-tts",
        "voice": "female"
    },
    "zhipu": {
        "api_key": ZHIPU_API_KEY,
        "base_url": ZHIPU_API_BASE
    },
    "tencent": {
        "api_key": TENCENT_API_KEY,
        "base_url": "https://tokenhub.tencentmaas.com/v1/api/video"
    }
}
