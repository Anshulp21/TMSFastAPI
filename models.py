from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="To Do")
    due_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
