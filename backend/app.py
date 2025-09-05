from fastapi import FastAPI, UploadFile, File, Form
from embed import model
from vector_store import SimpleVectorDB
from llm import get_llm_answer

app = FastAPI()
vdb = SimpleVectorDB(dim=384)  # adjust as per embedding model

@app.post("/upload/")
async def upload(file: UploadFile):
    text = (await file.read()).decode()
    chunks = text.split('\n')  # or smarter chunking
    vectors = model.encode(chunks)
    vdb.add(vectors, chunks)
    return {"msg": "Uploaded!"}

@app.post("/query/")
async def query_api(q: str = Form(...)):
    vector = model.encode([q])
    context = "\n".join(vdb.search(vector, 3))
    answer = get_llm_answer(f"Context:\n{context}\n\nQuestion:{q}")
    return {"answer": answer, "context": context}
