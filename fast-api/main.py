from fastapi import FastAPI, Depends, HTTPException
from db import get_db,Base,engine,SessionLocal
from models import User
from schemas import UserSchema
from sqlalchemy.orm import session
app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return "Hello world"

@app.post("/adduser")
def add_user(request:UserSchema, db: session = Depends(get_db)):
    user = User(name = request.name,email = request.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/{user_email}")
def get_user(user_email, db:session = Depends(get_db)):
    user = db.query(User).filter_by(email = user_email).first()
    return user

@app.get("/users")
def get_user(db:session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.delete("/user/{user_id}")
def delete_user(user_id, db : session = Depends(get_db)):
    user = db.query(User).filter_by(id = user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return "user Deleted successfully"