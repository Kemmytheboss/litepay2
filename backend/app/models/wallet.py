from sqlalchemy import Column, BigInteger, String, Enum, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    balance = Column(String(50), default="0")
    currency = Column(String(10), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())