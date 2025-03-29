from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class DocumentBase(BaseModel):
    title: str
    document_type: Literal["cv", "cover_letter"]
    employer_name: Optional[str] = None
    job_title: Optional[str] = None

class DocumentCreate(DocumentBase):
    content: str

class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    employer_name: Optional[str] = None
    job_title: Optional[str] = None

class DocumentResponse(DocumentBase):
    id: str
    user_id: str
    content: str
    file_path: Optional[str] = None
    file_url: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class DocumentGenerateRequest(BaseModel):
    """Request model for generating a document"""
    document_type: Literal["cv", "cover_letter"]
    employer_name: Optional[str] = None
    job_title: Optional[str] = None
    job_description: Optional[str] = None
    use_all_experiences: bool = True
    experience_ids: Optional[List[str]] = None
    education_ids: Optional[List[str]] = None
    achievement_ids: Optional[List[str]] = None