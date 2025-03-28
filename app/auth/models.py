from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.sql import func

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    # Subscription status
    subscription_status = Column(String, default="free")  # free, trial, active, canceled
    subscription_end_date = Column(DateTime, nullable=True)
    stripe_customer_id = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
