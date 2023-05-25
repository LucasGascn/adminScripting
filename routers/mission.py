from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from typing import List
from appsql import schemas
from cruds import crud_mission
import time

router = APIRouter()


# POST Function
@router.post("/missions/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    start_time = time.time()
    create_a_mission = crud_mission.create_mission(db=db, mission=mission)
    p = influxdb_client.Point("backend_measurement").tag("time", "mission").field("create_mission", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return create_a_mission


# GET Function
@router.get("/missions/", response_model=List[schemas.Mission])
def read_mission(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    start_time = time.time()
    mission = crud_mission.get_mission(db, skip=skip, limit=limit)
    p = influxdb_client.Point("backend_measurement").tag("time", "mission").field("get_missions", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return mission


# DELETE Function
@router.delete("/missions/{mission_id}")
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_mission = crud_mission.delete_mission(db=db, mission_id=mission_id)
    p = influxdb_client.Point("backend_measurement").tag("time", "mission").field("delete_mission", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return "Mission erased"


# PATCH Function
@router.patch("/missions/{mission_id}", response_model=schemas.Mission)
def update_mission(mission_id: int, mission: schemas.MissionUpdate, db: Session = Depends(get_db)):
    start_time = time.time()
    db_mission = crud_mission.patch_mission(db=db, mission_id=mission_id, mission=mission)
    p = influxdb_client.Point("backend_measurement").tag("time", "mission").field("patch_mission", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_mission


# PUT Function
@router.put("/missions/{mission_id}", response_model=schemas.Mission)
def change_mission(mission: schemas.MissionCreate, mission_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_mission = crud_mission.put_mission(db, mission_id=mission_id, mission=mission)
    p = influxdb_client.Point("backend_measurement").tag("time", "mission").field("put_mission", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_mission
