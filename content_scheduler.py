from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

class ContentScheduler:
    def __init__(self):
        self.optimal_time = self._get_optimal_time()

    def _get_optimal_time(self):
        # Placeholder: Use YouTube Analytics or a simple rule (e.g., 6 PM IST)
        return datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)

    def schedule_content(self, keyword):
        schedule_time = self.optimal_time + timedelta(days=1)
        return f"Schedule content for '{keyword}' at {schedule_time.strftime('%Y-%m-%d %H:%M IST')}"

# To use it:
scheduler = ContentScheduler()
print(scheduler.schedule_content("Python Tutorial"))