import httpx
from typing import Optional, Dict, Any
from config import ZHIPU_API_KEY, ZHIPU_API_BASE, API_CONFIG


class TextService:
    def __init__(self):
        self.api_key = ZHIPU_API_KEY
        self.base_url = ZHIPU_API_BASE
        self.config = API_CONFIG["text"]

    async def generate_text(
        self,
        prompt: str,
        task_type: str = "generate",
        system_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        task_prompts = {
            "generate": f"请根据以下要求生成文本内容：{prompt}",
            "polish": f"请润色以下文本，使其更加流畅和专业：{prompt}",
            "rewrite": f"请改写以下文本，用不同的表达方式呈现相同的内容：{prompt}",
            "summary": f"请为以下内容生成简洁的摘要：{prompt}",
            "optimize": f"请优化以下提示词，使其更加清晰和有效：{prompt}"
        }

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        else:
            messages.append({
                "role": "system",
                "content": "你是一个专业的AI助手，擅长文本生成、润色、改写、摘要和提示词优化。"
            })

        messages.append({
            "role": "user",
            "content": task_prompts.get(task_type, task_prompts["generate"])
        })

        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": self.config["model"],
                        "messages": messages,
                        "temperature": self.config["temperature"],
                        "max_tokens": self.config["max_tokens"]
                    }
                )
                response.raise_for_status()
                data = response.json()

                return {
                    "success": True,
                    "content": data["choices"][0]["message"]["content"],
                    "model": data.get("model", self.config["model"]),
                    "usage": data.get("usage", {})
                }
            except httpx.HTTPStatusError as e:
                return {
                    "success": False,
                    "error": f"API请求失败: {str(e)}",
                    "content": self._get_mock_response(prompt, task_type)
                }
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "content": self._get_mock_response(prompt, task_type)
                }

    def _get_mock_response(self, prompt: str, task_type: str) -> str:
        mock_responses = {
            "generate": f"根据您的要求，以下是生成的文本内容：{prompt[:50]}...\n\n这是一段由AI生成的示例文本。在实际部署时，这里将显示智谱AI生成的完整回复。",
            "polish": f"润色后的文本：\n\n{prompt}\n\n[润色建议已应用，使文本更加流畅和专业。]",
            "rewrite": f"改写后的文本：\n\n[已使用不同的表达方式重新呈现原文内容。]",
            "summary": f"内容摘要：\n\n本文主要讨论了相关内容，核心要点包括：\n1. 主要主题和观点\n2. 关键信息和数据\n3. 总结和建议",
            "optimize": f"优化后的提示词：\n\n{prompt}\n\n[已添加更清晰的指令和约束条件，提升提示词效果。]"
        }
        return mock_responses.get(task_type, mock_responses["generate"])


text_service = TextService()
