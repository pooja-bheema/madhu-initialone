# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/message")
def get_message():
    return {"message": "Hello from FastAPI backend!"}
