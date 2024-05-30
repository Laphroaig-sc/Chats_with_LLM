from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
 
 
app = FastAPI()
app.mount("/static", StaticFiles(directory="/app/static"), name="static")
templates = Jinja2Templates(directory="/app/templates")
 
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
 
@app.post("/question/")
async def ask_question(request: Request, user_input: str = Form(...)):
    # Send user questions to the LLM server
    response = requests.post("http://llm/answer/", json={"question": user_input})
    # Receive a response from the LLM server
    response_data = response.json()
    # Return replies from the LLM server to the user
    return templates.TemplateResponse("form.html", {"request": request, "question": user_input, "context": response_data['context'], "answer": response_data['answer']})