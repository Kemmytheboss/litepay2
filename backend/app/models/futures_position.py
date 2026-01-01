from sqlalchemy import Column, BigInteger, String, DECIMAL, Enum, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class FuturesPosition(Base):
    __tablename__ = "futures_positions"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    symbol = Column(String(20))
    side = Column(Enum("long", "short"))
    leverage = Column(Integer)
    entry_price = Column(DECIMAL(18, 8))
    quantity = Column(DECIMAL(18, 8))
    margin = Column(DECIMAL(18, 8))
    liquidation_price = Column(DECIMAL(18, 8))
    status = Column(Enum("open", "closed", "liquidated"), default="open")
    opened_at = Column(TIMESTAMP, server_default=func.now())
    closed_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())