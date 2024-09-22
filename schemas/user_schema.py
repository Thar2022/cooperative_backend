from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    sername: str
    lastname: str
    tell: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
