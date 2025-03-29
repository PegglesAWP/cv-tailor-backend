from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import User, Experience, Education, Achievement
from app.schemas import (
    ExperienceCreate, ExperienceResponse, ExperienceUpdate,
    EducationCreate, EducationResponse, EducationUpdate,
    AchievementCreate, AchievementResponse, AchievementUpdate
)
from app.auth.deps import get_current_active_user
from app.auth import generate_uuid

router = APIRouter()

# Experience endpoints
@router.post("/experiences", response_model=ExperienceResponse)
def create_experience(
    experience_in: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new work experience for current user.
    """
    experience_data = experience_in.dict()
    experience_data["id"] = generate_uuid()
    experience_data["user_id"] = current_user.id
    
    db_experience = Experience(**experience_data)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    
    return db_experience

@router.get("/experiences", response_model=List[ExperienceResponse])
def read_experiences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all experiences for current user.
    """
    experiences = db.query(Experience).filter(Experience.user_id == current_user.id).all()
    return experiences

@router.get("/experiences/{experience_id}", response_model=ExperienceResponse)
def read_experience(
    experience_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get a specific experience by ID.
    """
    experience = db.query(Experience).filter(
        Experience.id == experience_id,
        Experience.user_id == current_user.id
    ).first()
    
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found"
        )
    
    return experience

@router.put("/experiences/{experience_id}", response_model=ExperienceResponse)
def update_experience(
    experience_id: str,
    experience_in: ExperienceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a specific experience.
    """
    experience = db.query(Experience).filter(
        Experience.id == experience_id,
        Experience.user_id == current_user.id
    ).first()
    
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found"
        )
    
    # Update experience with provided fields
    for field, value in experience_in.dict(exclude_unset=True).items():
        setattr(experience, field, value)
    
    db.add(experience)
    db.commit()
    db.refresh(experience)
    
    return experience

@router.delete("/experiences/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experience(
    experience_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a specific experience.
    """
    experience = db.query(Experience).filter(
        Experience.id == experience_id,
        Experience.user_id == current_user.id
    ).first()
    
    if not experience:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found"
        )
    
    db.delete(experience)
    db.commit()
    
    return None

# Education endpoints
@router.post("/educations", response_model=EducationResponse)
def create_education(
    education_in: EducationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new education entry for current user.
    """
    education_data = education_in.dict()
    education_data["id"] = generate_uuid()
    education_data["user_id"] = current_user.id
    
    db_education = Education(**education_data)
    db.add(db_education)
    db.commit()
    db.refresh(db_education)
    
    return db_education

@router.get("/educations", response_model=List[EducationResponse])
def read_educations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all education entries for current user.
    """
    educations = db.query(Education).filter(Education.user_id == current_user.id).all()
    return educations

@router.get("/educations/{education_id}", response_model=EducationResponse)
def read_education(
    education_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get a specific education entry by ID.
    """
    education = db.query(Education).filter(
        Education.id == education_id,
        Education.user_id == current_user.id
    ).first()
    
    if not education:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Education not found"
        )
    
    return education

@router.put("/educations/{education_id}", response_model=EducationResponse)
def update_education(
    education_id: str,
    education_in: EducationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a specific education entry.
    """
    education = db.query(Education).filter(
        Education.id == education_id,
        Education.user_id == current_user.id
    ).first()
    
    if not education:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Education not found"
        )
    
    # Update education with provided fields
    for field, value in education_in.dict(exclude_unset=True).items():
        setattr(education, field, value)
    
    db.add(education)
    db.commit()
    db.refresh(education)
    
    return education

@router.delete("/educations/{education_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_education(
    education_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a specific education entry.
    """
    education = db.query(Education).filter(
        Education.id == education_id,
        Education.user_id == current_user.id
    ).first()
    
    if not education:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Education not found"
        )
    
    db.delete(education)
    db.commit()
    
    return None

# Achievement endpoints
@router.post("/achievements", response_model=AchievementResponse)
def create_achievement(
    achievement_in: AchievementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new achievement for current user.
    """
    achievement_data = achievement_in.dict()
    achievement_data["id"] = generate_uuid()
    achievement_data["user_id"] = current_user.id
    
    db_achievement = Achievement(**achievement_data)
    db.add(db_achievement)
    db.commit()
    db.refresh(db_achievement)
    
    return db_achievement

@router.get("/achievements", response_model=List[AchievementResponse])
def read_achievements(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all achievements for current user.
    """
    achievements = db.query(Achievement).filter(Achievement.user_id == current_user.id).all()
    return achievements

@router.get("/achievements/{achievement_id}", response_model=AchievementResponse)
def read_achievement(
    achievement_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get a specific achievement by ID.
    """
    achievement = db.query(Achievement).filter(
        Achievement.id == achievement_id,
        Achievement.user_id == current_user.id
    ).first()
    
    if not achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Achievement not found"
        )
    
    return achievement

@router.put("/achievements/{achievement_id}", response_model=AchievementResponse)
def update_achievement(
    achievement_id: str,
    achievement_in: AchievementUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a specific achievement.
    """
    achievement = db.query(Achievement).filter(
        Achievement.id == achievement_id,
        Achievement.user_id == current_user.id
    ).first()
    
    if not achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Achievement not found"
        )
    
    # Update achievement with provided fields
    for field, value in achievement_in.dict(exclude_unset=True).items():
        setattr(achievement, field, value)
    
    db.add(achievement)
    db.commit()
    db.refresh(achievement)
    
    return achievement

@router.delete("/achievements/{achievement_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_achievement(
    achievement_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a specific achievement.
    """
    achievement = db.query(Achievement).filter(
        Achievement.id == achievement_id,
        Achievement.user_id == current_user.id
    ).first()
    
    if not achievement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Achievement not found"
        )
    
    db.delete(achievement)
    db.commit()
    
    return None