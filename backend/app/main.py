from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="TextForge API",
    description="Convert text into DOCX and PDF documents",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def home():
    return {
        "message":"Welcome to TextForge API",
        "status":"running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}