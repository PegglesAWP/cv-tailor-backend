from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Dict, Any
from datetime import datetime

class EmployerBase(BaseModel):
    name: str
    website: Optional[str] = None
    industry: Optional[str] = None
    description: Optional[str] = None

class EmployerCreate(EmployerBase):
    values: Optional[List[str]] = None
    keywords: Optional[List[str]] = None

class EmployerUpdate(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    description: Optional[str] = None
    values: Optional[List[str]] = None
    keywords: Optional[List[str]] = None

class EmployerResponse(EmployerBase):
    id: str
    values: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    last_scraped: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ScrapeRequest(BaseModel):
    """Request to scrape employer data"""
    employer_url: str