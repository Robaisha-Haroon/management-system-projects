%%writefile crud.py
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker 

# Application Initialization
app = FastAPI()

# Database Configuration
database_url = "sqlite:///./todo.db" 
engine = create_engine(database_url, connect_args={"check_same_threads": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 

# Database Schema Definition
class TaskDB(Base):   
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)    
    title = Column(String)      
    is_done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)      

# Request Validation Schema
class TaskCreate(BaseModel):
    id: int
    title: str
    is_done: bool = False

# API Routes
@app.post("/tasks")
def add_tasks(new_task: TaskCreate):
    db = SessionLocal()  
    # Reference new_task schema attributes instead of undefined task_data
    db_task = TaskDB(
        id= new_task.id,
        title= new_task.title,
        is_done= new_task.is_done
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return {"status": "success", "data": new_task}

@app.get("/tasks")
def show_tasks():
    db = SessionLocal()
    tasks = db.query(TaskDB).all()
    db.close()
    return tasks
