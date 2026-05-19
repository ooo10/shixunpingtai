import httpx
import base64
from typing import Optional, Dict, Any
from config import ZHIPU_API_KEY, ZHIPU_API_BASE, API_CONFIG


class AudioService:
    def __init__(self):
        self.api_key = ZHIPU_API_KEY
        self.base_url = ZHIPU_API_BASE
        self.config = API_CONFIG["audio"]

    async def text_to_speech(
        self,
        text: str,
        voice: Optional[str] = None,
        speed: float = 1.0
    ) -> Dict[str, Any]:
        voice = voice or self.config["voice"]

        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/audio/speech",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "glm-tts",
                        "input": text,
                        "voice": voice,
                        "speed": speed,
                        "volume": 1.0,
                        "response_format": "wav"
                    }
                )
                response.raise_for_status()

                audio_base64 = base64.b64encode(response.content).decode('utf-8')
                return {
                    "success": True,
                    "audio_base64": audio_base64,
                    "audio_url": f"data:audio/wav;base64,{audio_base64[:100]}...",
                    "model": "glm-tts"
                }
            except httpx.HTTPStatusError as e:
                print(f"API Error: {e.response.text}")
                return {
                    "success": False,
                    "error": f"语音合成API请求失败: {str(e)}",
                    "audio_url": self._get_mock_audio_url(),
                    "model": "glm-tts"
                }
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "audio_url": self._get_mock_audio_url(),
                    "model": "glm-tts"
                }

    async def speech_to_text(
        self,
        audio_url: str
    ) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/audio/transcriptions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "cosyvoice-v2",
                        "audio_url": audio_url
                    }
                )
                response.raise_for_status()
                data = response.json()

                return {
                    "success": True,
                    "text": data.get("text", ""),
                    "model": "cosyvoice-v2"
                }
            except httpx.HTTPStatusError as e:
                return {
                    "success": False,
                    "error": f"语音识别API请求失败: {str(e)}",
                    "text": "语音识别失败，请稍后重试"
                }
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "text": "语音识别失败，请稍后重试"
                }

    def _get_mock_audio_url(self) -> str:
        return "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"


audio_service = AudioService()