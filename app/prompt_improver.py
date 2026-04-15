from app.llm import generate
from db.vector_store import search_similar

def improve_prompt(prompt, failure):
    context = "\n".join(search_similar(prompt))

    query = f"""
    Improve this prompt:

    Past fixes:
    {context}

    Original: {prompt}
    Issue: {failure}

    Return improved prompt.
    """

    return generate(query)