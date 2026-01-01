from sqlalchemy import Column, BigInteger, String, DECIMAL, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class SpotTrade(Base):
    __tablename__ = "spot_trades"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    symbol = Column(String(20))
    side = Column(Enum("buy", "sell"))
    quantity = Column(DECIMAL(18, 8))
    price = Column(DECIMAL(18, 8))
    fee = Column(DECIMAL(18, 8), default=0)
    status = Column(Enum("filled", "cancelled", "failed"), default="filled")
    executed_at = Column(TIMESTAMP, server_default=func.now())
    created_at = Column(TIMESTAMP, server_default=func.now())