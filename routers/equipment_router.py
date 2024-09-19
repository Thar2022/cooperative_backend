from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.equipment_controller import EquipmentController
from schemas.equipment_schema import EquipmentCreate, EquipmentUpdate, Equipment
from database import get_db

router = APIRouter()

@router.get("/equipment/", response_model=list[Equipment])
def getAll_equipment(db: Session = Depends(get_db)):
    return EquipmentController.getAll_equipment(db=db)

@router.post("/equipment/", response_model=Equipment)
def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    return EquipmentController.create_equipment(db=db, equipment=equipment)

@router.get("/equipment/{equipment_id}", response_model=Equipment)
def getById_equipment(equipment_id: int, db: Session = Depends(get_db)):
    return EquipmentController.getById_equipment(db=db, equipment_id=equipment_id)

@router.put("/equipment/{equipment_id}", response_model=Equipment)
def update_equipment(equipment_id: int, equipment: EquipmentUpdate, db: Session = Depends(get_db)):
    return EquipmentController.update_equipment(db=db, equipment_id=equipment_id, equipment=equipment)

@router.delete("/equipment/{equipment_id}", response_model=dict)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    return EquipmentController.delete_equipment(db=db, equipment_id=equipment_id)
