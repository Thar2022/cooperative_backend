from pydantic import BaseModel
from typing import Optional

class PlaceEquipmentBase(BaseModel):
    place_id: int
    equipment_id: int
    stock: int
    available_stock: int

class PlaceEquipmentCreate(PlaceEquipmentBase):
    pass

class PlaceEquipmentUpdate(BaseModel):
    place_id: Optional[int] = None
    equipment_id: Optional[int] = None
    stock: Optional[int] = None
    available_stock: Optional[int] = None

class PlaceEquipment(PlaceEquipmentBase):
    place_equipment_id: int

    class Config:
        from_attributes  = True
