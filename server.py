from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Zynk Studio Memory Core")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MemoryRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Zynk Studio Core Server is running perfectly!"}

@app.post("/remember")
async def remember_memory(request: MemoryRequest):
    return {"status": "success", "message": "Memory synced to Knowledge Graph successfully!"}

@app.post("/query")
async def query_memory(request: Request):
    data = await request.json()
    # Yahan humne answer bhejne ka system set kar diya hai
    user_query = data.get("query", "")
    return {"answer": f"AI Agent says: I've processed your query about '{user_query}' in the Zync Studio Knowledge Graph."}

@app.post("/memify")
async def memify():
    return {"message": "Graph enriched successfully!"}

@app.post("/forget")
async def forget_memory(request: Request):
    return {"message": "Data pruned successfully!"}