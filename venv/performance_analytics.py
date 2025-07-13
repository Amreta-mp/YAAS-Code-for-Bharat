from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

class PerformanceAnalytics:
    def __init__(self):
        self.api_key = os.getenv("youtube_api_key")
        # Changed 'youtubeAnalytics' to 'youtube' and 'v2' to 'v3'
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_video_metrics(self, video_id):
        try:
            response = self.youtube.videos().list(
                part="statistics",
                id=video_id
            ).execute()
            if response['items']:
                stats = response['items'][0]['statistics']
                # The 'dislikeCount' field has been removed from the YouTube Data API v3 as of December 13, 2021.
                # It will always return 0 or be absent. Consider removing it if accurate dislikes are needed (which is no longer possible via API).
                return [stats.get('viewCount', '0'), stats.get('likeCount', '0'), stats.get('dislikeCount', '0'), stats.get('commentCount', '0')]
            return ["No data"]
        except Exception as e:
            return f"Error fetching metrics: {str(e)}"

analytics = PerformanceAnalytics()