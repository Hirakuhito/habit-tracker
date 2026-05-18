from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    color = Column(String, default="#3B82F6")
    created_at = Column(DateTime, server_default=func.now())

    logs = relationship("HabitLog", back_populates="habit", cascade="all, delete")


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    date = Column(Date, nullable=False)
    completed = Column(Boolean, default=False)

    habit = relationship("Habit", back_populates="logs")
