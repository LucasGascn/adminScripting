from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from depedency import get_db
from appsql import schemas
from cruds import crud_qg

router = APIRouter()


# POST Function
@router.post("/qg/", response_model=schemas.QG)
def create_qg(qg: schemas.QGCreate, db: Session = Depends(get_db)):
    return crud_qg.create_qg(db=db, qg=qg)


# GET Function
@router.get("/qg/", response_model=List[schemas.QG])
def read_qg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qg = crud_qg.get_qg(db, skip=skip, limit=limit)
    return qg


# DELETE Function
@router.delete("/qg/{qg_id}")
def delete_qg(qg_id: int, db: Session = Depends(get_db)):
    db_qg = crud_qg.delete_qg(db, qg_id=qg_id)
    return "Quarter General deconstruct"


# PUT Function
@router.put("/qg/{qg_id}", response_model=schemas.QG)
def change_qg(qg: schemas.QGCreate, qg_id: int, db: Session = Depends(get_db)):
    db_qg = crud_qg.put_qg(db, qg_id=qg_id, qg=qg)
    return db_qg

# PATCH Function


