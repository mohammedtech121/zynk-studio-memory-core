import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Zynk Studio Memory Core Initialization
app = FastAPI(title="Zynk Studio Memory Core")

# 🚀 Vercel ko VIP Pass (CORS Setup) - Cloud connection ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vercel ko allow karne ke liye
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# UI se aane wale data ka structure
class MemoryRequest(BaseModel):
    text: str

# Test karne ke liye basic route
@app.get("/")
async def root():
    return {"message": "Zynk Studio Core Server is running perfectly!"}

# Tera main Autonomous Agent endpoint jo UI se connect hoga
@app.post("/remember")
async def remember_memory(request: MemoryRequest):
    try:
        client_text = request.text
        print(f"New Client Requirement Received: {client_text}")
        
        # (Yahan tera Cognee ya RAG ka jo bhi processing logic hai wo backend mein chalega)
        
        # UI ko success message bhejna
        return {
            "status": "success", 
            "message": "Memory synced to Knowledge Graph successfully!",
            "data": client_text
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}