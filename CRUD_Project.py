%%writefile main.py 

# crud project

from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
todo_list = []

class Task(BaseModel):
    id: int
    title: str
    is_done: bool= False

@app.get("/tasks")
def get_all_tasks():
    return {"Tasks": todo_list}

@app.post("/tasks")
def create_tasks(new_task : Task):
    todo_list.append(new_task)
    return {"Message": "Task has been added successfully"}

@app.put("/tasks/{task_id}")
def update_tasks(task_id: int, updated_task: Task):
    for i in range(len(todo_list)):
        if todo_list[i].id == task_id:
            todo_list[i] = updated_task
            return {"tasks": "task updated"}
    return {"Error": "Task not found" }

@app.delete("/tasks")
def delete_tasks(unwant_task : Task):
    for i in todo_list:
        if i in todo_list:
            todo_list.remove(unwant_task)
            return {"Message" : "Task has been removed successfully"}
        return {"Error" : "Task not found"}
