from models import Base
from database import engine

Base.metadata.create_all(bind=engine)
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import TaskCreate, TaskUpdate
from crud import create_task, get_tasks, get_task, update_task, delete_task
from auth import create_token, get_current_user

app = FastAPI()
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login/")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "admin":
        return {"access_token": create_token(request.username), "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/tasks/")
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return create_task(db, task)

@app.get("/tasks/")
def list_tasks(db: Session = Depends(get_db), current_user: str = Depends(get_current_user), status: str = None):
    return get_tasks(db, status=status)

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=404, detail=f"Task with ID {task_id} not found"
        )
    return task


@app.put("/tasks/{task_id}")
def modify_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    updated_task = update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    deleted_task = delete_task(db, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
