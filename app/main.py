from fastapi import FastAPI
from app.analyzer import analyze_failure
from app.prompt_improver import improve_prompt
from app.evaluator import compare
from db.vector_store import add_to_memory, load_memory
from app.llm import generate

app = FastAPI()
load_memory()

@app.post("/analyze")
def analyze(data: dict):
    prompt = data["prompt"]
    output = data["output"]

    failure = analyze_failure(prompt, output)
    improved_prompt = improve_prompt(prompt, failure)

    new_output = generate(improved_prompt)

    scores = compare(prompt, output, improved_prompt, new_output)

    add_to_memory(prompt, failure, improved_prompt)

    return {
        "failure": failure,
        "improved_prompt": improved_prompt,
        "new_output": new_output,
        "scores": scores
    }