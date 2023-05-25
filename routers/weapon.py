from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_weapon
from typing import List
import time

router = APIRouter()


# GET Function
@router.post("/weapons/", response_model=schemas.Weapon)
def create_weapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)):
    start_time = time.time()
    create_a_weapon = crud_weapon.create_weapon(db=db, weapon=weapon)
    p = influxdb_client.Point("backend_measurement").tag("time", "weapon").field("get_weapon", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return create_a_weapon


# POST Function
@router.get("/weapons/", response_model=List[schemas.Weapon])
def read_weapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    start_time = time.time()
    weapons = crud_weapon.get_weapon(db, skip=skip, limit=limit)
    p = influxdb_client.Point("backend_measurement").tag("time", "weapon").field("create_weapon", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return weapons


# DELETE function
@router.delete("/weapons/{weapon_id}")
def delete_weapon(weapon_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_weapon = crud_weapon.delete_weapon(db, weapon_id=weapon_id)
    p = influxdb_client.Point("backend_measurement").tag("time", "weapon").field("delete_weapon", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return "Weapon is obsolete"


# PATCH function
@router.patch("/weapons/{weapons_id}", response_model=schemas.Weapon)
def update_weapon(weapon_id: int, weapons: schemas.WeaponUpdate, db: Session = Depends(get_db)):
    start_time = time.time()
    db_weapon = crud_weapon.patch_weapon(db=db, weapon_id=weapon_id,  weapon=weapons)
    p = influxdb_client.Point("backend_measurement").tag("time", "weapon").field("patch_weapon", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_weapon


# PUT function
@router.put("/weapons/{weapon_id}", response_model=schemas.Weapon)
def change_weapon(weapon: schemas.WeaponCreate, weapon_id: int, db: Session = Depends(get_db)):
    db_weapon = crud_weapon.put_weapon(db, weapon_id=weapon_id, weapon=weapon)
    p = influxdb_client.Point("backend_measurement").tag("time", "weapon").field("put_weapon", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_weapon
