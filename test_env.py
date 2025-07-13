from dotenv import load_dotenv
import os

load_dotenv()
print("llm_provider:", os.getenv("llm_provider"))
print("mistral_api_key:", os.getenv("mistral_api_key"))
print("youtube_api_key:", os.getenv("youtube_api_key"))