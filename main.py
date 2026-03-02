from fastapi import FastAPI
from app.db.base import engine, Base
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User
from fastapi import Body, Depends
from app.db.session import get_db
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/user/", response_model=UserResponse)
def root(user: UserCreate = Body(...), db: Session = Depends(get_db)):
    user = User(username=user.username, email=user.email, password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/user/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users