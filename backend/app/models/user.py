from sqlalchemy import Column, BigInteger, String, Enum, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum("user", "admin"), default="user")
    referral_code = Column(String(12), unique=True)
    referred_by = Column(BigInteger, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())