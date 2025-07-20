from multi_llm import MultiLLM
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM
llm = MultiLLM()

def generate_script(keyword="python tutorials", tone="friendly", style="educational"):
    """
    Generate a video script with intro, body, and conclusion based on keyword and preferences.
    Args:
        keyword (str): The topic for the script (default: "python tutorials").
        tone (str): The tone of the script (default: "friendly", e.g., "professional", "casual").
        style (str): The style of the script (default: "educational", e.g., "narrative", "step-by-step").
    Returns:
        dict: Script with intro, body, and conclusion.
    """
    prompt = f"""
Generate a video script for the topic '{keyword}'.
- Tone: {tone}.
- Style: {style}.
Include the following sections:
1. Introduction (30-50 words): Hook the audience and introduce the topic.
2. Body (100-150 words): Provide detailed content, examples, or steps.
3. Conclusion (30-50 words): Summarize and call to action.
"""
    response = llm._call([{"role": "user", "content": prompt}])
    # Parse the response (assuming multi_llm returns a string with sections)
    # This parsing assumes the LLM strictly follows the numbering and exact phrases "1. Introduction", "2. Body", "3. Conclusion"
    # A more robust parsing might be needed if the LLM's output format varies.
    try:
        intro_part = response.split("2. Body")[0]
        body_part = response.split("2. Body")[1].split("3. Conclusion")[0]
        conclusion_part = response.split("3. Conclusion")[1]

        script = {
            "introduction": intro_part.replace("1. Introduction", "").strip(),
            "body": body_part.strip(),
            "conclusion": conclusion_part.strip()
        }
    except IndexError:
        # Fallback if parsing fails, e.g., LLM didn't format as expected
        print("Warning: Failed to parse script into sections. Returning full response as body.")
        script = {
            "introduction": "Could not parse introduction.",
            "body": response, # Return full response as body if parsing fails
            "conclusion": "Could not parse conclusion."
        }
    return script

if __name__ == "__main__":
    script = generate_script("python tutorials", "friendly", "step-by-step")
    print("Introduction:", script["introduction"])
    print("Body:", script["body"])
    print("Conclusion:", script["conclusion"])