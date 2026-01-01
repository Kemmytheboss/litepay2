from sqlalchemy import Column, BigInteger, String, DECIMAL, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    asset = Column(String(20))
    amount = Column(DECIMAL(18, 8))
    tx_hash = Column(String(255), unique=True)
    status = Column(Enum("pending", "confirmed", "rejected"), default="pending")
    created_at = Column(TIMESTAMP, server_default=func.now())
    confirmed_at = Column(TIMESTAMP)
