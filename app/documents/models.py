from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func

from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"))

    title = Column(String)
    content = Column(Text)
    document_type = Column(Enum("cv", "cover_letter", name="document_type"))

    employer_name = Column(String, nullable=True)
    job_title = Column(String, nullable=True)

    file_path = Column(String, nullable=True)
    file_url = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
