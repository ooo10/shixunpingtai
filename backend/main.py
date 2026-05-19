from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn
import httpx

from services.text_service import text_service
from services.image_service import image_service
from services.video_service import video_service
from services.audio_service import audio_service

app = FastAPI(title="AIGC Training Platform API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    prompt: str
    task_type: str = "generate"
    system_prompt: Optional[str] = None

class ImageRequest(BaseModel):
    prompt: str
    size: Optional[str] = None
    quality: Optional[str] = None
    style: Optional[str] = None

class VideoRequest(BaseModel):
    prompt: str
    duration: Optional[int] = None
    fps: Optional[int] = None

class AudioRequest(BaseModel):
    text: str
    voice: Optional[str] = None
    speed: float = 1.0

class ImageToImageRequest(BaseModel):
    prompt: str
    image_url: str
    strength: float = 0.7

class SpeechToTextRequest(BaseModel):
    audio_url: str

@app.get("/")
async def root():
    return {
        "message": "AIGC Training Platform API",
        "version": "1.0.0",
        "endpoints": {
            "text": "/api/text/generate",
            "image": "/api/image/generate",
            "video": "/api/video/generate",
            "audio": "/api/audio/tts"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/text/generate")
async def generate_text(request: TextRequest):
    result = await text_service.generate_text(
        prompt=request.prompt,
        task_type=request.task_type,
        system_prompt=request.system_prompt
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/api/image/generate")
async def generate_image(request: ImageRequest):
    result = await image_service.generate_image(
        prompt=request.prompt,
        size=request.size,
        quality=request.quality,
        style=request.style
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/api/image/image-to-image")
async def image_to_image(request: ImageToImageRequest):
    result = await image_service.image_to_image(
        prompt=request.prompt,
        image_url=request.image_url,
        strength=request.strength
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/api/video/generate")
async def generate_video(request: VideoRequest):
    result = await video_service.generate_video(
        prompt=request.prompt,
        duration=request.duration,
        fps=request.fps
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.get("/api/video/proxy")
async def proxy_video(url: str):
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.get(url)
            if response.status_code == 403:
                fallback_url = "https://www.w3schools.com/html/mov_bbb.mp4"
                response = await client.get(fallback_url)
            
            headers = dict(response.headers)
            headers.pop('content-length', None)
            headers['Access-Control-Allow-Origin'] = '*'
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=headers,
                media_type=response.headers.get('content-type', 'video/mp4')
            )
    except Exception as e:
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                fallback_url = "https://www.w3schools.com/html/mov_bbb.mp4"
                response = await client.get(fallback_url)
                headers = dict(response.headers)
                headers.pop('content-length', None)
                headers['Access-Control-Allow-Origin'] = '*'
                return Response(
                    content=response.content,
                    status_code=response.status_code,
                    headers=headers,
                    media_type=response.headers.get('content-type', 'video/mp4')
                )
        except Exception as fallback_e:
            raise HTTPException(status_code=500, detail=str(fallback_e))

@app.post("/api/audio/tts")
async def text_to_speech(request: AudioRequest):
    result = await audio_service.text_to_speech(
        text=request.text,
        voice=request.voice,
        speed=request.speed
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/api/audio/stt")
async def speech_to_text(request: SpeechToTextRequest):
    result = await audio_service.speech_to_text(
        audio_url=request.audio_url
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
