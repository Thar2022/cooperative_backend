from sqlalchemy import Column, Integer, String
from database import Base

class Equipment(Base):
    __tablename__ = 'equipment'

    equipment_id = Column(Integer, primary_key=True, index=True)
    equipment_name = Column(String, index=True)

    def __repr__(self):
        return f"<Equipment(name={self.equipment_name})>"