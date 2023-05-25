from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from depedency import get_db
from appsql import schemas
from cruds import crud_qg
import time
router = APIRouter()


# POST Function
@router.post("/qg/", response_model=schemas.QG)
def create_qg(qg: schemas.QGCreate, db: Session = Depends(get_db)):
    start_time = time.time()
    create_a_qg = crud_qg.create_qg(db=db, qg=qg)
    p = influxdb_client.Point("backend_measurement").tag("time", "qg").field("create_qg", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return create_a_qg


# GET Function
@router.get("/qg/", response_model=List[schemas.QG])
def read_qg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    start_time = time.time()
    qg = crud_qg.get_qg(db, skip=skip, limit=limit)
    p = influxdb_client.Point("backend_measurement").tag("time", "qg").field("get_qg", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return qg


# DELETE Function
@router.delete("/qg/{qg_id}")
def delete_qg(qg_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_qg = crud_qg.delete_qg(db, qg_id=qg_id)
    p = influxdb_client.Point("backend_measurement").tag("time", "qg").field("delete_qg", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return "Quarter General deconstruct"


# PUT Function
@router.put("/qg/{qg_id}", response_model=schemas.QG)
def change_qg(qg: schemas.QGCreate, qg_id: int, db: Session = Depends(get_db)):
    start_time = time.time()
    db_qg = crud_qg.put_qg(db, qg_id=qg_id, qg=qg)
    p = influxdb_client.Point("backend_measurement").tag("time", "qg").field("put_qg", str(time.time() - start_time))
    write_api.write(bucket=bucket, org=org, record=p)
    return db_qg

# PATCH Function


