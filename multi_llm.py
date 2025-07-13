from typing import Any, Optional, List
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class MultiLLM:
    provider: str = os.getenv("llm_provider", "mistral")
    mistral_api_key: str = os.getenv("mistral_api_key", "")

    def __init__(self):
        if self.provider != "mistral":
            raise ValueError("Only Mistral is supported.")

    def _call(self, messages: List[dict], **kwargs) -> str:
        headers = {"Authorization": f"Bearer {self.mistral_api_key}"}
        try:
            response = requests.post(
                "https://api.mistral.ai/v1/chat/completions",
                json={
                    "model": "mistral-small",
                    "messages": messages,
                    "max_tokens": 200
                },
                headers=headers
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    @property
    def _llm_type(self) -> str:
        return "mistral_llm"