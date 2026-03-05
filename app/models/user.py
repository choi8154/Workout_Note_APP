from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)
    muscle_mass = Column(Integer, nullable=True)
    fat_mass = Column(Integer, nullable=True)
    created_at = Column(DateTime, func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())