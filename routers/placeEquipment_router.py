from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.placeEquipment_controller import PlaceEquipmentController
from schemas.placeEquipment_schema import PlaceEquipmentCreate, PlaceEquipmentUpdate, PlaceEquipment,PlaceEquipmentResponse
from database import get_db

router = APIRouter()

@router.get("/place_equipment/", response_model=list[PlaceEquipmentResponse])
def getAll_placeEquipment(db: Session = Depends(get_db)):
    return PlaceEquipmentController.getAll_placeEquipment(db=db)

@router.get("/place_equipment/place/{place_id}", response_model=list[PlaceEquipmentResponse])
def getAll_placeEquipment(place_id: int,db: Session = Depends(get_db)):
    return PlaceEquipmentController.get_place_equipment_by_place_id(db=db,place_id=place_id)

@router.post("/place_equipment/", response_model=PlaceEquipment)
def create_placeEquipment(place_equipment: PlaceEquipmentCreate, db: Session = Depends(get_db)):
    return PlaceEquipmentController.create_placeEquipment(db=db, place_equipment=place_equipment)

@router.get("/place_equipment/{place_equipment_id}", response_model=PlaceEquipmentResponse)
def getById_placeEquipment(place_equipment_id: int, db: Session = Depends(get_db)):
    return PlaceEquipmentController.getById_placeEquipment(db=db, place_equipment_id=place_equipment_id)
 
@router.put("/place_equipment/{place_equipment_id}", response_model=PlaceEquipment)
def update_placeEquipment(place_equipment_id: int, place_equipment: PlaceEquipmentUpdate, db: Session = Depends(get_db)):
    return PlaceEquipmentController.update_placeEquipment(db=db, place_equipment_id=place_equipment_id, place_equipment=place_equipment)

@router.delete("/place_equipment/{place_equipment_id}", response_model=dict)
def delete_placeEquipment(place_equipment_id: int, db: Session = Depends(get_db)):
    return PlaceEquipmentController.delete_placeEquipment(db=db, place_equipment_id=place_equipment_id)