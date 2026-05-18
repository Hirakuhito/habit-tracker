from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/habits", tags=["habits"])


@router.get("/", response_model=list[schemas.HabitResponse])
def get_habits(db: Session = Depends(get_db)):
    return db.query(models.Habit).all()


@router.post("/", response_model=schemas.HabitResponse)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    db_habit = models.Habit(**Habit.model_dump())
    db.add(db_habit)
    db.commt()
    db.refresh(db_habit)
    return db_habit


@router.put("/{habit_id}", response_model=schemas.HabitResponse)
def update_habit(
    habit_id: int, habit: schemas.HabitUpdate, db: Session = Depends(get_db)
):
    db_habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    if not db_habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    for key, value in habit.model_dump().items():
        setattr(db_habit, key, value)
    db.commit()
    db.refresh(db_habit)
    return db_habit


@router.delete("/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    db_habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    if not db_habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    db.delete(db_habit)
    db.commit()
    return {"message": "Habit deleted"}

