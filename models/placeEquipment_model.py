from sqlalchemy import Column, Integer
from database import Base

class PlaceEquipment(Base):
    __tablename__ = 'place_equipment'

    place_equipment_id = Column(Integer, primary_key=True, index=True)
    place_id = Column(Integer, index=True)
    equipment_id = Column(Integer,index=True)
    stock = Column(Integer,index=True)
    available_stock = Column(Integer,index=True)
