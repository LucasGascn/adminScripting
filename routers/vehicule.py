from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_vehicule
from typing import List
import time
#from uvicorn.config import LOGGING_CONFIG

router = APIRouter()

# LOGGING_CONFIG["formatters"]["access"]["fmt"] = (
#         "%(asctime)s " + LOGGING_CONFIG["formatters"]["access"]["fmt"]
# )
# GET Function
@router.get("/vehicules/", response_model=List[schemas.Vehicule])
def read_vehicule(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    start_time = time.time()
    vehicule = crud_vehicule.get_vehicule(db, skip=skip, limit=limit)
    print(time.time() - start_time)
    p = influxdb_client.Point("backend_measurement").tag("time", "vehicule").field("get_vehicules", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return vehicule


# POST Function
@router.post("/vehicules/", response_model=schemas.Vehicule)
def create_vehicule(vehicule: schemas.VehiculeCreate, db: Session = Depends(get_db)):
    start_time = time.time()
    create_a_vehicule = crud_vehicule.create_vehicule(db=db, vehicule=vehicule)
    print(time.time() - start_time)
    p = influxdb_client.Point("backend_measurement").tag("time", "vehicule").field("create_vehicule", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return create_a_vehicule


# DELETE Function
@router.delete("/vehicules/{vehicule_id}")
def delete_qg(vehicule_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_vehicule = crud_vehicule.delete_vehicule(db, vehicule_id=vehicule_id)
    p = influxdb_client.Point("backend_measurement").tag("time", "vehicule").field("delete_vehicule", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return "Vehicule is obsolete now"


# Patch Function
@router.patch("/vehicules/{vehicule_id}", response_model=schemas.Vehicule)
def update_vehicule(vehicule_id: int, vehicule: schemas.VehiculeUpdate, db: Session = Depends(get_db)):
    start_time = time.time()
    db_vehicule = crud_vehicule.patch_vehicule(db=db, vehicule_id=vehicule_id, vehicule=vehicule)
    p = influxdb_client.Point("backend_measurement").tag("time", "vehicule").field("patch_vehicule", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_vehicule


# PUT Function
@router.put("/vehicules/{vehicule_id}", response_model=schemas.Vehicule)
def change_vehicule(vehicule: schemas.VehiculeCreate, vehicule_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_vehicule = crud_vehicule.put_vehicule(db, vehicule_id=vehicule_id, vehicule=vehicule)
    p = influxdb_client.Point("backend_measurement").tag("time", "vehicule").field("put_vehicule", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_vehicule
