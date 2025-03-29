from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import User, Employer
from app.schemas import EmployerCreate, EmployerResponse, EmployerUpdate, ScrapeRequest
from app.auth.deps import get_current_active_user
from app.auth import generate_uuid

router = APIRouter()

@router.get("/", response_model=List[EmployerResponse])
def read_employers(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all employers from the database.
    """
    employers = db.query(Employer).all()
    return employers

@router.get("/{employer_id}", response_model=EmployerResponse)
def read_employer(
    employer_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get a specific employer by ID.
    """
    employer = db.query(Employer).filter(Employer.id == employer_id).first()
    
    if not employer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employer not found"
        )
    
    return employer

@router.post("/scrape", response_model=EmployerResponse)
def scrape_employer(
    request: ScrapeRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Scrape employer information from a URL.
    
    This is a placeholder for the actual scraping functionality.
    In a real implementation, this would:
    1. Scrape the employer website
    2. Extract company values and keywords
    3. Create or update the employer in the database
    """
    # For now, create a simple employer with placeholder data
    employer_name = request.employer_url.split('//')[-1].split('/')[0].replace('www.', '')
    
    # Check if employer already exists
    employer = db.query(Employer).filter(Employer.name == employer_name).first()
    
    if employer:
        # Return existing employer
        return employer
    
    # Create new employer with placeholder data
    employer_data = {
        "id": generate_uuid(),
        "name": employer_name,
        "website": request.employer_url,
        "industry": "Technology",  # Placeholder
        "description": f"This is a placeholder description for {employer_name}",
        "values": ["innovation", "teamwork", "customer-focus"],  # Placeholder values
        "keywords": ["technology", "software", "development"]  # Placeholder keywords
    }
    
    db_employer = Employer(**employer_data)
    db.add(db_employer)
    db.commit()
    db.refresh(db_employer)
    
    return db_employer