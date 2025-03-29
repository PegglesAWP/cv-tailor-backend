from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Experience schemas
class ExperienceBase(BaseModel):
    company_name: str
    job_title: str
    start_date: datetime
    end_date: Optional[datetime] = None
    is_current: bool = False
    location: Optional[str] = None
    description: Optional[str] = None

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceUpdate(BaseModel):
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_current: Optional[bool] = None
    location: Optional[str] = None
    description: Optional[str] = None

class ExperienceResponse(ExperienceBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Education schemas
class EducationBase(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: datetime
    end_date: Optional[datetime] = None
    is_current: bool = False
    location: Optional[str] = None
    description: Optional[str] = None

class EducationCreate(EducationBase):
    pass

class EducationUpdate(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_current: Optional[bool] = None
    location: Optional[str] = None
    description: Optional[str] = None

class EducationResponse(EducationBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

# Achievement schemas
class AchievementBase(BaseModel):
    title: str
    description: str
    date: Optional[datetime] = None

class AchievementCreate(AchievementBase):
    pass

class AchievementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None

class AchievementResponse(AchievementBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True