from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import sys
import os
from pathlib import Path

# Add parent directory to path to import memo_structurizer
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from memo_structurizer import MemoStructurizer
from config import get_settings

app = FastAPI(
    title="Memo Structurizer API",
    description="Structure your messy memos into organized Markdown files",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class MemoRequest(BaseModel):
    content: str
    memo_type: Optional[str] = None
    title: Optional[str] = None

class MemoResponse(BaseModel):
    structured_content: str
    memo_type: str
    saved_path: Optional[str] = None
    created_at: str

class HealthResponse(BaseModel):
    status: str
    timestamp: str

# Initialize
settings = get_settings()
structurizer = MemoStructurizer(base_dir=settings.base_directory)

# Routes
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat()
    )

@app.post("/structure", response_model=MemoResponse)
async def structure_memo(request: MemoRequest):
    """
    Structure a memo based on its content and type.
    
    - **content**: The memo content (required)
    - **memo_type**: Type of memo - 'meeting', 'learning', 'interview', or 'idea' (optional)
    - **title**: Custom title for the memo (optional)
    """
    try:
        if not request.content.strip():
            raise HTTPException(status_code=400, detail="Memo content cannot be empty")
        
        # Process the memo
        result = structurizer.process_memo(
            content=request.content,
            memo_type=request.memo_type,
            title=request.title
        )
        
        return MemoResponse(
            structured_content=result['structured_content'],
            memo_type=result['memo_type'],
            saved_path=result.get('saved_path'),
            created_at=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/save-to-github")
async def save_to_github(request: MemoRequest):
    """
    Structure memo and save directly to GitHub.
    Requires GITHUB_TOKEN and GITHUB_REPO environment variables.
    """
    try:
        if not settings.github_token:
            raise HTTPException(
                status_code=400,
                detail="GitHub token not configured"
            )
        
        result = structurizer.process_memo(
            content=request.content,
            memo_type=request.memo_type,
            title=request.title,
            save_to_github=True,
            github_token=settings.github_token
        )
        
        return JSONResponse(
            status_code=200,
            content={
                "message": "Memo saved to GitHub successfully",
                "memo_type": result['memo_type'],
                "github_url": result.get('github_url'),
                "created_at": datetime.now().isoformat()
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memo-types")
async def get_memo_types():
    """
    Get available memo types
    """
    return {
        "types": [
            {"value": "meeting", "label": "📋 Meeting", "description": "Meeting notes and decisions"},
            {"value": "learning", "label": "📚 Learning", "description": "Learning notes and concepts"},
            {"value": "interview", "label": "🎤 Interview", "description": "Interview and feedback notes"},
            {"value": "idea", "label": "💡 Idea", "description": "Ideas and brainstorming"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
