from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "To Do"
    due_date: date

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    due_date: Optional[date]

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
