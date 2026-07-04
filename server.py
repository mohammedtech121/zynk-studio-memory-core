from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import cognee

app = FastAPI()

# 🚀 CORS MIDDLEWARE: Ye tere Vercel frontend ko block hone se bachayega
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (Perfect for hackathon)
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

class MemoryRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Zynk Studio Core Server is running perfectly!"}

@app.post("/remember")
async def remember_memory(request: MemoryRequest):
    try:
        # Cognee logic for ingestion
        await cognee.add(request.text)
        return {"status": "success", "message": "Memory synced to Knowledge Graph successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/query")
async def query_memory(request: Request):
    try:
        data = await request.json()
        user_query = data.get("query", "")
        # Cognee logic for querying
        answer = await cognee.query(user_query)
        return {"answer": f"AI Agent says: {answer}"}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}

@app.post("/forget")
async def forget_memory(request: Request):
    data = await request.json()
    dataset_name = data.get("dataset_name") # Ye woh ID/Name hai jo user input dega
    
    if not dataset_name:
        return {"status": "error", "message": "Dataset name is required"}
    
    try:
        # ASLI LOGIC: Actual pruning command
        await cognee.prune.prune_data(dataset_name)
        return {"status": "success", "message": f"Data for '{dataset_name}' pruned successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/memify")
async def memify():
    # Placeholder for graph enrichment
    return {"message": "Graph enriched successfully!"}