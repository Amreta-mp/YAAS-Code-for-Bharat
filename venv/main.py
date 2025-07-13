from fastapi import FastAPI
from seo_agent import run_workflow
import uvicorn

app = FastAPI()

@app.get("/optimize/")
async def optimize(keyword: str = "tech reviews"):
    result = run_workflow(keyword)
    return {
        "seo_analysis": result["analysis"],
        "schedule": result["schedule"],
        "performance_metrics": result["metrics"],
        "thumbnail_idea": result["thumbnail_idea"],
        "generated_content": result["content"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)