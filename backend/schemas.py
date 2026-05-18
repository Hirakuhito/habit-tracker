from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


# --- Habit ---
class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None
    color: Optional[str] = "#3B82F6"


class HabitCreate(HabitBase):
    pass


class HabitUpdate(HabitBase):
    pass


class HabitResponse(HabitBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# --- HabitLog ---
class HabitLogBase(BaseModel):
    habit_id: int
    date: date
    completed: bool = False


class HabitLogCreate(HabitLogBase):
    pass


class HabitLogResponse(HabitLogBase):
    id: int

    class Config:
        from_attributes = True
