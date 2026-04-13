from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    username: str
    email: str
    age: int

app=FastAPI()

@app.post("/register/")
async def register_user(user:User):
    return user