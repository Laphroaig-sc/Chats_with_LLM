from fastapi import FastAPI
from pydantic import BaseModel
import requests
from llm_generator import response_by_llm


# Validation, serialisation
class Question_LLM(BaseModel):
    question: str

app = FastAPI()

@app.post("/answer/")
async def answer_question(question_llm: Question_LLM):
    # TO DB Server
    response = requests.post("http://db/DB/", json={"question": question_llm.question})

    # context
    context = response.json()['context']

    # LMM operation
    answer = response_by_llm(context, question_llm.question)
    # answer = 'debug'+question_llm.question

    # TO WEB SERVER
    return {"context": context, "answer": answer}