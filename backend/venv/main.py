# -----------------------------------------------------------
# main.py
#
# This is the entry point of our backend.
# It creates a FastAPI app with one basic route ("/")
# to test if our server is working correctly.
#
# We will later add:
# - Google Drive watcher
# - OCR Agent
# - Classification Agent (Groq)
# - RAG Engine
# - Email Agent
# - Multi-Agent Orchestration
#
# But for now, we start small & clean.
# -----------------------------------------------------------

from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI(
    title="Document Worker Backend",
    description="Multi-agent automation system for documents",
    version="1.0.0"
)

# -----------------------------------------------------------
# Basic health check route
# Purpose:
# - To verify backend is running
# - Frontend and deployment services use this route
# -----------------------------------------------------------


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!",
        "status": "healthy"
    }
