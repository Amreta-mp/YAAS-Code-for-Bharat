from multi_llm import MultiLLM
from youtube_tool import youtube_tool
from content_scheduler import scheduler
from performance_analytics import analytics
from thumbnail_generator import generator
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize components
llm = MultiLLM()

def run_workflow(keyword="tech reviews"):
    # Analyze keyword
    youtube_data = youtube_tool(keyword)
    prompt = f"Analyze this YouTube data for SEO: {youtube_data}. Suggest a keyword and optimization tips."
    analysis = llm._call([{"role": "user", "content": prompt}])

    # Schedule content
    schedule = scheduler.schedule_content(keyword)

    # Analyze performance
    video_id = "YOUR_VIDEO_ID_HERE"  # Replace with actual logic
    metrics = analytics.get_video_metrics(video_id)

    # Generate thumbnail
    thumbnail_idea = generator.generate_thumbnail_idea(keyword)

    # Generate content
    prompt = f"Based on this SEO analysis: {analysis}. Generate a 100-word blog post."
    content = llm._call([{"role": "user", "content": prompt}])

    return {
        "analysis": analysis,
        "schedule": schedule,
        "metrics": metrics,
        "thumbnail_idea": thumbnail_idea,
        "content": content
    }

if __name__ == "__main__":
    result = run_workflow()
    print("SEO Analysis:", result.get("analysis"))
    print("Schedule:", result.get("schedule"))
    print("Performance Metrics:", result.get("metrics"))
    print("Thumbnail Idea:", result.get("thumbnail_idea"))
    print("Generated Content:", result.get("content"))