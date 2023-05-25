from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_vehicule
from typing import List


router = APIRouter()


# GET Function
@router.get("/vehicules/", response_model=List[schemas.Vehicule])
def read_vehicule(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicule = crud_vehicule.get_vehicule(db, skip=skip, limit=limit)
    return vehicule


# POST Function
@router.post("/vehicules/", response_model=schemas.Vehicule)
def create_vehicule(vehicule: schemas.VehiculeCreate, db: Session = Depends(get_db)):
    return crud_vehicule.create_vehicule(db=db, vehicule=vehicule)


# DELETE Function
@router.delete("/vehicules/{vehicule_id}")
def delete_qg(vehicule_id: int, db: Session = Depends(get_db)):
    db_vehicule = crud_vehicule.delete_vehicule(db, vehicule_id=vehicule_id)
    return "Vehicule is obsolete now"


# Patch Function
@router.patch("/vehicules/{vehicule_id}", response_model=schemas.Vehicule)
def update_vehicule(vehicule_id: int, vehicule: schemas.VehiculeUpdate, db: Session = Depends(get_db)):
    db_vehicule = crud_vehicule.patch_vehicule(db=db, vehicule_id=vehicule_id, vehicule=vehicule)
    return db_vehicule


# PUT Function
@router.put("/vehicules/{vehicule_id}", response_model=schemas.Vehicule)
def change_vehicule(vehicule: schemas.VehiculeCreate, vehicule_id: int, db: Session = Depends(get_db)):
    db_vehicule = crud_vehicule.put_vehicule(db, vehicule_id=vehicule_id, vehicule=vehicule)
    return db_vehicule
