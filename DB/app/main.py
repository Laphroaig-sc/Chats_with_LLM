from fastapi import FastAPI
from pydantic import BaseModel
from rag import search_by_rag
 
 
class DB(BaseModel):
    question: str
 
app = FastAPI()
 
@app.post("/DB/")
async def cite_data(question_db: DB):
 
    # RAG operation
    serch_cnt=2
    results = search_by_rag(question=question_db.question, serch_num=serch_cnt)
    citation_data=''
    for i in range(serch_cnt):
        citation_data += results[i].page_content + '\n'
 
    # Return to web server
    return {"context": citation_data}