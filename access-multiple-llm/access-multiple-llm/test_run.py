from llm_factory import LLMFactory
from system_prompt import prompt_generate_summary
def generate_summary(text):
    """
    Generates a summary of the given text using the LLM.
    """
    response = LLMFactory.invoke(
        system_prompt=prompt_generate_summary,
        human_message=text,
        temperature=0.7,
        local_llm=False,
    )
    summary = response.content.strip()
    return summary



if __name__ == "__main__":
    Question = "What is the impact of climate change in global trade?"
    summary = generate_summary(Question)
    print("\nGenerated Summary:")
    print(summary)