from fastapi import FastAPI  

app = FastAPI()

@app.get("/")
def home():
    return {"message": "This is my first API project"}  

@app.get("/student")
def student():
    return {
        "Name": "Ali",
        "Age": 22,
        "Course": "Python"  
    }

@app.get("/teacher") 
def teacher():
    return {
        "Name": "Majid",
        "Subject": "Python"
    }
