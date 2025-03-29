# Import all schemas for easy importing
from app.schemas.user import UserBase, UserCreate, UserUpdate, UserResponse, Token, TokenPayload
from app.schemas.experience import (
    ExperienceBase, ExperienceCreate, ExperienceUpdate, ExperienceResponse,
    EducationBase, EducationCreate, EducationUpdate, EducationResponse,
    AchievementBase, AchievementCreate, AchievementUpdate, AchievementResponse
)
from app.schemas.document import DocumentBase, DocumentCreate, DocumentUpdate, DocumentResponse, DocumentGenerateRequest
from app.schemas.employer import EmployerBase, EmployerCreate, EmployerUpdate, EmployerResponse, ScrapeRequest