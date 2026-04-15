from app.llm import generate
from db.vector_store import search_similar

def analyze_failure(prompt, output):
    context = "\n".join(search_similar(prompt + output))

    query = f"""
    You are an expert in debugging LLM outputs.

    Past similar failures:
    {context}

    Prompt: {prompt}
    Output: {output}

    Classify into:
    hallucination / missing_context / bad_reasoning / ambiguous_prompt

    Give reason.
    """

    return generate(query)