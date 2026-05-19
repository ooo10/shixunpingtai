import httpx
import urllib.parse
from typing import Optional, Dict, Any
from config import API_CONFIG


class ImageService:
    def __init__(self):
        self.config = API_CONFIG["image"]

    async def generate_image(
        self,
        prompt: str,
        style: Optional[str] = None,
        size: Optional[str] = None,
        quality: Optional[str] = None
    ) -> Dict[str, Any]:
        image_size = size or self.config["size"]
        width, height = image_size.split("x")
        
        try:
            if isinstance(prompt, bytes):
                prompt = prompt.decode('utf-8')
            encoded_prompt = urllib.parse.quote(prompt, safe='')
            image_url = f"https://pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux"
            
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.get(image_url, follow_redirects=True)
                if response.status_code == 200:
                    return {
                        "success": True,
                        "image_url": image_url,
                        "model": "flux",
                        "provider": "Pollinations AI"
                    }

            return {
                "success": True,
                "image_url": self._get_mock_image_url(prompt),
                "model": "mock",
                "provider": "Mock"
            }

        except Exception as e:
            print(f"Pollinations AI调用失败，使用Mock图片: {str(e)}")
            return {
                "success": True,
                "image_url": self._get_mock_image_url(prompt),
                "model": "mock",
                "provider": "Mock"
            }

    def _get_mock_image_url(self, prompt: str) -> str:
        return f"https://picsum.photos/1280/1280?random={hash(prompt) % 100}"


image_service = ImageService()