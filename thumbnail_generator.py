from multi_llm import MultiLLM
import os
from dotenv import load_dotenv

load_dotenv()

class ThumbnailGenerator:
    def __init__(self):
        self.llm = MultiLLM()

    def generate_thumbnail_idea(self, keyword):
        prompt = f"Suggest a thumbnail idea for a YouTube video about '{keyword}'. Include colors, text, and key elements."
        response = self.llm._call([{"role": "user", "content": prompt}])
        return response

generator = ThumbnailGenerator()