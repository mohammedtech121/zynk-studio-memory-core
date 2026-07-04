import os
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
    # Yahan tumhara AI/Cognee logic aayega
    return {"answer": f"AI Recall: I remember you mentioned '{data.get('query')}'"}

@app.post("/memify")
async def memify():
    return {"message": "Graph enriched successfully!"}

@app.post("/forget")
async def forget_memory(request: Request):
    return {"message": "Data pruned successfully!"}