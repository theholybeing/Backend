from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI SQLite CRUD")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/")
def create(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students/")
def read_all(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.put("/students/{student_id}")
def update(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated = crud.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@app.delete("/students/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_student(db, student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Deleted successfully"}