from sqlalchemy import Column, Integer, DateTime, String, DECIMAL, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    customer_email = Column(String)
    total = Column(DECIMAL)
