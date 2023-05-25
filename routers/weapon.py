from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_weapon
from typing import List


router = APIRouter()


# GET Function
@router.post("/weapons/", response_model=schemas.Weapon)
def create_weapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)):
    return crud_weapon.create_weapon(db=db, weapon=weapon)


# POST Function
@router.get("/weapons/", response_model=List[schemas.Weapon])
def read_weapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weapons = crud_weapon.get_weapon(db, skip=skip, limit=limit)
    return weapons


# DELETE function
@router.delete("/weapons/{weapon_id}")
def delete_weapon(weapon_id: int, db: Session = Depends(get_db)):
    db_weapon = crud_weapon.delete_weapon(db, weapon_id=weapon_id)
    return "Weapon is obsolete"


# PATCH function
@router.patch("/weapons/{weapons_id}", response_model=schemas.Weapon)
def update_weapon(weapon_id: int, weapons: schemas.WeaponUpdate, db: Session = Depends(get_db)):
    db_weapon = crud_weapon.patch_weapon(db=db, weapon_id=weapon_id,  weapon=weapons)
    return db_weapon


# PUT function
@router.put("/weapons/{weapon_id}", response_model=schemas.Weapon)
def change_weapon(weapon: schemas.WeaponCreate, weapon_id: int, db: Session = Depends(get_db)):
    db_weapon = crud_weapon.put_weapon(db, weapon_id=weapon_id, weapon=weapon)
    return db_weapon
