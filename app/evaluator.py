from app.llm import generate

def score(prompt, output):
    query = f"""
    Rate output quality from 0 to 10.

    Prompt: {prompt}
    Output: {output}

    Only return number.
    """

    try:
        return float(generate(query).strip())
    except:
        return 5.0


def compare(old_p, old_o, new_p, new_o):
    old_score = score(old_p, old_o)
    new_score = score(new_p, new_o)

    improvement = 0 if old_score == 0 else ((new_score - old_score) / old_score) * 100

    return {
        "old_score": old_score,
        "new_score": new_score,
        "improvement_%": round(improvement, 2)
    }
