from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_competitor_data(keyword: str) -> str:
    api_key = os.getenv("youtube_api_key")
    if not api_key:
        return "Error: YouTube API key not found in .env"
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            q=keyword,
            part='snippet',
            type='video',
            maxResults=3,
            order='viewCount'
        )
        response = request.execute()
        videos = [
            {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'tags': item['snippet'].get('tags', [])
            }
            for item in response.get('items', [])
        ]
        return str(videos)
    except Exception as e:
        return f"Error fetching YouTube data: {str(e)}"

# Tool is simply a reference to the function
youtube_tool = fetch_competitor_data
