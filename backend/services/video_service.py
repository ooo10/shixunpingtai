import httpx
import asyncio
from typing import Optional, Dict, Any
from config import API_CONFIG


class VideoService:
    def __init__(self):
        self.config = API_CONFIG["video"]

    async def generate_video(
        self,
        prompt: str,
        duration: Optional[int] = None,
        style: Optional[str] = None,
        fps: Optional[int] = None
    ) -> Dict[str, Any]:
        video_duration = duration or 5

        video_url = self._get_mock_video_url(prompt)
        proxy_url = f"/api/video/proxy?url={httpx.QueryParams({'url': video_url})}"

        return {
            "success": True,
            "video_id": f"vid_{hash(prompt)}_{video_duration}",
            "video_url": proxy_url,
            "status": "completed",
            "model": "mock",
            "provider": "演示视频"
        }

    def _get_mock_video_url(self, prompt: str) -> str:
        video_categories = {
            '猫': [
                'https://assets.mixkit.co/videos/preview/mixkit-cat-sitting-on-a-sofa-looking-at-the-camera-4720-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-two-cats-sitting-on-the-sofa-1488-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-kitten-playing-in-the-grass-1400-large.mp4'
            ],
            '狗': [
                'https://assets.mixkit.co/videos/preview/mixkit-golden-retriever-puppy-sitting-and-looking-at-the-camera-4724-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-dog-running-on-the-beach-1188-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-pug-dog-sitting-on-the-floor-4725-large.mp4'
            ],
            '熊': [
                'https://assets.mixkit.co/videos/preview/mixkit-bear-standing-on-hind-legs-in-the-forest-4829-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-brown-bear-walking-in-the-forest-4828-large.mp4'
            ],
            '动物': [
                'https://assets.mixkit.co/videos/preview/mixkit-deer-standing-in-the-forest-4830-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-birds-flying-over-the-ocean-1176-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-fish-swimming-in-the-ocean-1175-large.mp4'
            ],
            '风景': [
                'https://assets.mixkit.co/videos/preview/mixkit-beautiful-mountain-landscape-with-fog-2481-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-waterfall-in-the-middle-of-the-forest-4831-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-forest-stream-in-the-sunlight-4832-large.mp4'
            ],
            '自然': [
                'https://assets.mixkit.co/videos/preview/mixkit-leaves-falling-from-a-tree-1179-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-waves-crashing-on-the-beach-1181-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-sun-setting-over-the-ocean-1184-large.mp4'
            ],
            '海洋': [
                'https://assets.mixkit.co/videos/preview/mixkit-ocean-waves-crashing-on-the-shore-1183-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-underwater-view-of-fish-swimming-1180-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-dolphins-jumping-out-of-the-water-1178-large.mp4'
            ],
            '日落': [
                'https://assets.mixkit.co/videos/preview/mixkit-sunset-over-the-mountains-1185-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-sun-setting-over-a-lake-4833-large.mp4'
            ],
            '城市': [
                'https://assets.mixkit.co/videos/preview/mixkit-city-traffic-at-night-1193-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-modern-city-skyline-at-sunset-4834-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-city-buildings-at-night-1192-large.mp4'
            ],
            '人': [
                'https://assets.mixkit.co/videos/preview/mixkit-happy-young-woman-walking-in-the-park-4835-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-man-running-in-the-park-1196-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-couple-walking-on-the-beach-1197-large.mp4'
            ],
            '人物': [
                'https://assets.mixkit.co/videos/preview/mixkit-people-walking-in-the-city-1194-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-woman-doing-yoga-in-the-morning-4836-large.mp4'
            ],
            '食物': [
                'https://assets.mixkit.co/videos/preview/mixkit-delicious-food-on-a-plate-4837-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-cooking-pasta-in-a-pan-1198-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-fresh-vegetables-on-a-table-4838-large.mp4'
            ],
            '水果': [
                'https://assets.mixkit.co/videos/preview/mixkit-fresh-fruits-in-a-bowl-4839-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-red-apples-on-a-tree-4840-large.mp4'
            ],
            '葡萄': [
                'https://assets.mixkit.co/videos/preview/mixkit-grapes-hanging-from-the-vine-4841-large.mp4'
            ],
            '苹果': [
                'https://assets.mixkit.co/videos/preview/mixkit-red-apples-on-a-tree-4840-large.mp4'
            ],
            '香蕉': [
                'https://assets.mixkit.co/videos/preview/mixkit-bananas-hanging-from-a-tree-4842-large.mp4'
            ],
            '花': [
                'https://assets.mixkit.co/videos/preview/mixkit-beautiful-pink-flowers-in-the-garden-4843-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-red-roses-in-a-vase-4844-large.mp4'
            ],
            '植物': [
                'https://assets.mixkit.co/videos/preview/mixkit-green-plants-in-a-garden-4845-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-trees-swaying-in-the-wind-1200-large.mp4'
            ],
            '树': [
                'https://assets.mixkit.co/videos/preview/mixkit-tree-branches-swaying-in-the-wind-4846-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-pine-trees-in-the-forest-4847-large.mp4'
            ],
            '森林': [
                'https://assets.mixkit.co/videos/preview/mixkit-dense-forest-with-sunlight-filtering-through-4848-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-forest-path-in-the-morning-4849-large.mp4'
            ],
            '汽车': [
                'https://assets.mixkit.co/videos/preview/mixkit-red-sports-car-driving-on-the-road-1202-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-traffic-on-a-highway-1203-large.mp4'
            ],
            '运动': [
                'https://assets.mixkit.co/videos/preview/mixkit-man-playing-basketball-1204-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-woman-running-on-the-beach-1205-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-soccer-player-kicking-the-ball-1206-large.mp4'
            ],
            '音乐': [
                'https://assets.mixkit.co/videos/preview/mixkit-musician-playing-the-guitar-4850-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-piano-player-playing-the-piano-4851-large.mp4'
            ],
            '舞蹈': [
                'https://assets.mixkit.co/videos/preview/mixkit-dancer-performing-a-contemporary-dance-4852-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-ballet-dancer-performing-on-stage-4853-large.mp4'
            ],
            '鸟': [
                'https://assets.mixkit.co/videos/preview/mixkit-birds-flying-over-the-ocean-1176-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-birds-singing-in-a-tree-4854-large.mp4'
            ],
            '鱼': [
                'https://assets.mixkit.co/videos/preview/mixkit-fish-swimming-in-the-ocean-1175-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-colorful-fish-in-an-aquarium-4855-large.mp4'
            ],
            '山': [
                'https://assets.mixkit.co/videos/preview/mixkit-mountain-range-at-sunset-4856-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-snowy-mountain-peak-4857-large.mp4'
            ],
            '河': [
                'https://assets.mixkit.co/videos/preview/mixkit-river-flowing-through-the-forest-4858-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-small-stream-in-the-woods-4859-large.mp4'
            ],
            '湖': [
                'https://assets.mixkit.co/videos/preview/mixkit-lake-surface-with-ripples-4860-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-sunset-over-a-lake-4833-large.mp4'
            ],
            '天空': [
                'https://assets.mixkit.co/videos/preview/mixkit-clouds-moving-across-the-sky-4861-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-blue-sky-with-white-clouds-4862-large.mp4'
            ],
            '星星': [
                'https://assets.mixkit.co/videos/preview/mixkit-stars-in-the-night-sky-4863-large.mp4'
            ],
            '月亮': [
                'https://assets.mixkit.co/videos/preview/mixkit-moon-in-the-night-sky-4864-large.mp4'
            ],
            '太阳': [
                'https://assets.mixkit.co/videos/preview/mixkit-sun-shining-brightly-in-the-sky-4865-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-sunrise-over-the-ocean-4866-large.mp4'
            ],
            '雪': [
                'https://assets.mixkit.co/videos/preview/mixkit-snow-falling-in-the-forest-4867-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-snowy-landscape-at-sunset-4868-large.mp4'
            ],
            '雨': [
                'https://assets.mixkit.co/videos/preview/mixkit-rain-drops-on-a-window-4869-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-rain-falling-on-the-ground-4870-large.mp4'
            ],
            '云': [
                'https://assets.mixkit.co/videos/preview/mixkit-clouds-moving-across-the-sky-4861-large.mp4'
            ],
            '海': [
                'https://assets.mixkit.co/videos/preview/mixkit-ocean-waves-crashing-on-the-shore-1183-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-sea-waves-at-sunset-4871-large.mp4'
            ],
            '沙滩': [
                'https://assets.mixkit.co/videos/preview/mixkit-beach-with-palm-trees-4872-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-people-relaxing-on-the-beach-4873-large.mp4'
            ],
            '城堡': [
                'https://assets.mixkit.co/videos/preview/mixkit-castle-in-the-mountains-4874-large.mp4'
            ],
            '房子': [
                'https://assets.mixkit.co/videos/preview/mixkit-modern-house-exterior-4875-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-cozy-cottage-in-the-forest-4876-large.mp4'
            ],
            '学校': [
                'https://assets.mixkit.co/videos/preview/mixkit-school-building-exterior-4877-large.mp4'
            ],
            '公园': [
                'https://assets.mixkit.co/videos/preview/mixkit-people-in-the-park-4878-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-park-with-benches-and-trees-4879-large.mp4'
            ],
            '花园': [
                'https://assets.mixkit.co/videos/preview/mixkit-beautiful-garden-with-flowers-4880-large.mp4',
                'https://assets.mixkit.co/videos/preview/mixkit-garden-path-with-roses-4881-large.mp4'
            ]
        }

        prompt_lower = prompt.lower()
        for keyword, videos in video_categories.items():
            if keyword in prompt_lower:
                return videos[hash(prompt) % len(videos)]

        default_videos = [
            "https://assets.mixkit.co/videos/preview/mixkit-nature-scene-with-trees-and-flowers-4882-large.mp4",
            "https://assets.mixkit.co/videos/preview/mixkit-beautiful-landscape-with-lake-4883-large.mp4",
            "https://assets.mixkit.co/videos/preview/mixkit-sunset-over-the-city-4884-large.mp4"
        ]
        return default_videos[hash(prompt) % len(default_videos)]


video_service = VideoService()