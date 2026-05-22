from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv('.env.local')
load_dotenv('.env')

class Settings(BaseSettings):
    # Application
    app_name: str = "Memo Structurizer API"
    debug: bool = True
    
    # Directory
    base_directory: str = os.path.expanduser("~/Documents/my-knowledge")
    
    # GitHub (Optional - for direct GitHub saving)
    github_token: Optional[str] = os.getenv("GITHUB_TOKEN")
    github_repo: Optional[str] = os.getenv("GITHUB_REPO")
    
    # CORS
    cors_origins: list = ["http://localhost:5173", "http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env.local"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()
