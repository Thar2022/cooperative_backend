from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_schema import UserCreate
# from database import get_db

def create_user(user: UserCreate, db: Session):
    db_user = User(
        user_name=user.user_name,
        password=user.password,
        sername=user.sername,
        lastname=user.lastname,
        tell=user.tell,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int, db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
