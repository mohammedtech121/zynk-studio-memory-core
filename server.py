import os
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import cognee
from dotenv import load_dotenv

# Env variables load karna (automatic API key utha lega)
load_dotenv()

app = FastAPI(title="Zynk Studio Memory Core")

# CORS config taaki frontend backend se securely connect kar sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input Validation Models
class MemoryInput(BaseModel):
    text: str

class QueryInput(BaseModel):
    query: str

class ForgetInput(BaseModel):
    dataset_name: str


# 1. Ingest Data (Remember)
@app.post("/remember")
async def add_memory(data: MemoryInput):
    try:
        await cognee.remember(data.text)
        return {"status": "success", "message": "Successfully structured into Cognee Cloud graph!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 2. Query Data (Recall)
@app.post("/recall")
async def get_memory(data: QueryInput):
    try:
        result = await cognee.recall(data.query)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 3. Enrich Graph (Improve/Memify)
@app.post("/improve")
async def optimize_memory():
    try:
        await cognee.improve()
        return {"status": "success", "message": "Memory graph enriched and memified successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 4. Prune Data (Forget)
@app.post("/forget")
async def delete_memory(data: ForgetInput):
    try:
        await cognee.forget(dataset=data.dataset_name)
        return {"status": "success", "message": f"Dataset '{data.dataset_name}' pruned cleanly."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    # Server run command (Error fixed and perfectly indented)
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)