from fastapi import FastAPI
from database import Base, engine
from routers import habits

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Habit Tracker API")

app.include_router(habits.router)


@app.get("/")
def read_root():
    return {"message": "hello, Habit Tracker!"}
