from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.user_controller import create_user, get_user
from schemas.user_schema import UserCreate, User
from database import get_db

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/users/{user_id}", response_model=User)
def get_user_route(user_id: int, db: Session = Depends(get_db)):
    return get_user(user_id, db)
