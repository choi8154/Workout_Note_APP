from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class WorkoutSet(Base):
    __tablename__ = 'workout_sets'

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    weight = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True) 
    weight = Column(Integer, nullable=True)
    reps = Column(Integer, nullable=False)
    duration = Column(Integer) 
    rest_time = Column(Integer) 
    memo = Column(String(255), nullable=True) 
    created_at = Column(Integer, nullable=False) 
    updated_at = Column(Integer, nullable=False) 

    workout = relationship("Workout", back_populates="sets")
    exercise = relationship("Exercise", back_populates="sets")