import os
import importlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routers.equipment_router import router as equipment_router
# from routers.place_routers import router as place_router
# from routers.placeEquipment_router import router as placeEquipment_router
from database import engine, Base
# สร้างฐานข้อมูล
Base.metadata.create_all(bind=engine)

app = FastAPI()

# กำหนด CORS (Cross-Origin Resource Sharing) ถ้าจำเป็น
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # เปลี่ยนเป็น URL ของคุณถ้าต้องการจำกัด
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# รวม router
<<<<<<< Updated upstream
app.include_router(equipment_router,tags=["Equipment"])
app.include_router(place_router,tags=["Place"])
app.include_router(placeEquipment_router,tags=["PlaceEquipment"])
=======
# app.include_router(equipment_router)
# app.include_router(place_router)
# app.include_router(placeEquipment_router)

# รวม router จากโฟลเดอร์ routers
router_folder = 'routers'
for filename in os.listdir(router_folder):
    if filename.endswith('.py') and filename != 'base.py':  # ไม่ต้องการรวมไฟล์เฉพาะ
        module_name = filename[:-3]  # ตัด '.py'
        module_path = f"{router_folder}.{module_name}"  # สร้าง path
        print(module_path)
        module = importlib.import_module(module_path)
        
        # # ตรวจสอบว่ามี router หรือไม่
        if hasattr(module, 'router'):
            app.include_router(module.router)
>>>>>>> Stashed changes


@app.get("/")
def read_root():
    return {"message": "Welcome to the Sports Equipment Rental System!"}
