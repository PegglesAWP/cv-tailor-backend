from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.sql import func

from app.database import Base

class Employer(Base):
    __tablename__ = "employers"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    website = Column(String, nullable=True)
    industry = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    
    values = Column(JSON, nullable=True)  # Store company values as JSON
    keywords = Column(JSON, nullable=True)  # Store relevant keywords as JSON
    
    last_scraped = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())