from sqlalchemy import Column, BigInteger, String, DECIMAL, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class Withdrawal(Base):
    __tablename__ = "withdrawals"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    asset = Column(String(20))
    amount = Column(DECIMAL(18, 8))
    address = Column(String(255))
    status = Column(Enum("pending", "approved", "rejected", "sent"), default="pending")
    tx_hash = Column(String(255))
    requested_at = Column(TIMESTAMP, server_default=func.now())
    processed_at = Column(TIMESTAMP)
    sent_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())