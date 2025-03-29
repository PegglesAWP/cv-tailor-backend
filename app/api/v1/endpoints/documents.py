from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import User, Document
from app.schemas import DocumentCreate, DocumentResponse, DocumentUpdate, DocumentGenerateRequest
from app.auth.deps import get_current_active_user
from app.auth import generate_uuid

router = APIRouter()

@router.post("/", response_model=DocumentResponse)
def create_document(
    document_in: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new document for current user.
    """
    document_data = document_in.dict()
    document_data["id"] = generate_uuid()
    document_data["user_id"] = current_user.id
    
    db_document = Document(**document_data)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    
    return db_document

@router.get("/", response_model=List[DocumentResponse])
def read_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all documents for current user.
    """
    documents = db.query(Document).filter(Document.user_id == current_user.id).all()
    return documents

@router.get("/{document_id}", response_model=DocumentResponse)
def read_document(
    document_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get a specific document by ID.
    """
    document = db.query(Document).filter(
        Document.id == document_id,
        Document.user_id == current_user.id
    ).first()
    
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    return document

@router.put("/{document_id}", response_model=DocumentResponse)
def update_document(
    document_id: str,
    document_in: DocumentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a specific document.
    """
    document = db.query(Document).filter(
        Document.id == document_id,
        Document.user_id == current_user.id
    ).first()
    
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    # Update document with provided fields
    for field, value in document_in.dict(exclude_unset=True).items():
        setattr(document, field, value)
    
    db.add(document)
    db.commit()
    db.refresh(document)
    
    return document

@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(
    document_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a specific document.
    """
    document = db.query(Document).filter(
        Document.id == document_id,
        Document.user_id == current_user.id
    ).first()
    
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    db.delete(document)
    db.commit()
    
    return None

@router.post("/generate", response_model=DocumentResponse)
def generate_document(
    request: DocumentGenerateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Generate a new document using AI based on user profile and preferences.
    
    This is a placeholder for the actual AI document generation functionality.
    In a real implementation, this would:
    1. Gather user experiences, education, and achievements
    2. Call the AI generation service
    3. Create and store the generated document
    """
    # For now, create a simple document with placeholder content
    document_data = {
        "id": generate_uuid(),
        "user_id": current_user.id,
        "title": f"Generated {request.document_type.capitalize()}",
        "content": f"This is a placeholder for a generated {request.document_type}",
        "document_type": request.document_type,
        "employer_name": request.employer_name,
        "job_title": request.job_title
    }
    
    db_document = Document(**document_data)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    
    return db_document