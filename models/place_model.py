from sqlalchemy import Column, Integer, String
from database import Base

class Place(Base):
    __tablename__ = 'place'

    place_id = Column(Integer, primary_key=True, index=True)
    place_name = Column(String, index=True)

    def __repr__(self):
        return f"<Place(name={self.place_name})>"