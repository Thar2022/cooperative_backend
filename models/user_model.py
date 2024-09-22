from sqlalchemy import Column, Integer, String, Text
from database import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    sername = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    tell = Column(String(10), nullable=False)
    role = Column(String(255), nullable=False)
