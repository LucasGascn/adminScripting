from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from typing import List
from cruds import crud_operator
import time
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "projectone"
org = "project"
token = "BKjW5CQlPW-x0xg8N2rRXRaFLlEMPaPMPOCXRfMXcUf9FJqTt3oWjxGeaozalW3IG2nitrvtNc7mmN1vhdh_RA=="
# Store the URL of your InfluxDB instance
url="http://192.168.64.17:8086"


client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

router = APIRouter()


"""
POST function
Use the request Schema for put the value send by request in db
GET function
Get the value push in db by the different request, use it for print in front
PATCH function
Get an instance already exist.
it's allow to change some value but not necessarily all values.
DELETE function
Get the instance ID and delete this
"""


# POST function
@router.post("/operators/", response_model=schemas.Operator)
def create_operator(operator: schemas.OperatorCreate, db: Session = Depends(get_db)):
    start_time = time.time()

    return crud_operator.create_operator(db=db, operator=operator)


# GET function
@router.get("/operators/", response_model=List[schemas.Operator])
def read_operators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    start_time = time.time()

    operators = crud_operator.get_operators(db, skip=skip, limit=limit)
    return operators


# By ID
@router.get("/operators/{operator_id}", response_model=schemas.Operator)
def read_operator(operator_id: int, db: Session = Depends(get_db)):
    start_time = time.time()

    db_operator = crud_operator.get_operator(db, operator_id=operator_id)
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    return db_operator


# By Weapon
@router.get("/operators/filter-weapon/{weapon_id}", response_model=List[schemas.Operator])
def read_operator_weapon(weapon_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.get_operator_weapon(db, weapon_id=weapon_id)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("get_operator_by_weapon", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator


# By Quarter General
@router.get("/operators/filter-qg/{qg_id}", response_model=List[schemas.Operator])
def read_operator_weapon(qg_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.get_operator_qg(db, qg_id=qg_id)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("get_operator_by_qg", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator

# By Mission
@router.get("/operators/filter-mission/{mission_id}", response_model=List[schemas.Operator])
def read_operator_mission(mission_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.get_operator_mission(db, mission_id=mission_id)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("get_operator_by_mission", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator


# By Name
@router.get("/operators/filter-name/{name}", response_model=List[schemas.Operator])
def read_operator_name(name: str, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.get_operator_name(db, name=name)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("get_operator_by_name", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator


# By Nationality
@router.get("/operators/filter-nationality/{nationality}", response_model=List[schemas.Operator])
def read_operator_nationality(nationality: str, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.get_operator_nationality(db, nationality=nationality)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("get_operator_by_nationality", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator


# Function DELETE
@router.delete("/operators/{operator_id}")
def delete_operator(operator_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.delete_operator(db, operator_id=operator_id)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("delete_operator", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return "Operator eliminated"


# Function PATCH
@router.patch("/operators/{operator_id}", response_model=schemas.Operator)
def update_operator(operator_id: int, operator: schemas.OperatorUpdate, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.patch_operator(db=db, operator_id=operator_id,  operator=operator)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("patch_operator", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator


# Function PUT
@router.put("/operators/{operator_id}", response_model=schemas.Operator)
def change_operator(operator: schemas.OperatorCreate, operator_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_operator = crud_operator.put_operator(db, operator_id=operator_id, operator=operator)
    p = influxdb_client.Point("backend_measurement").tag("total_time", "operator").field("put_operator", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_operator