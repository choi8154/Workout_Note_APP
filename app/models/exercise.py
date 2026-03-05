from sqlalchemy import Column, Integer, String, Text, Enum
from app.db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    target_area = Column(String(100), index=True)
    category = Column(Enum("하체", "상체", "코어", name="exercise_category"), index=True)
    created_at = Column(String(50))
    updated_at = Column(String(50))
    description = Column(Text)