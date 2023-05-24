from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET function
def get_vehicule(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicules).offset(skip).limit(limit).all()


# Create function
def create_vehicule(db: Session, vehicule: schemas.VehiculeCreate):
    db_vehicule = models.Vehicules(name=vehicule.name, type=vehicule.type)
    db.add(db_vehicule)
    db.commit()
    db.refresh(db_vehicule)
    return db_vehicule


# DELETE function
def delete_vehicule(db: Session, vehicule_id: int):
    db_vehicule = db.query(models.Vehicules).filter(models.Vehicules.id == vehicule_id).first()
    if db_vehicule is None:
        raise HTTPException(status_code=404, detail="Vehicule not found")
    db.delete(db_vehicule)
    db.commit()
    return db_vehicule


# PATCH function
def patch_vehicule(vehicule_id: int, db: Session, vehicule: schemas.VehiculeUpdate):
    db_vehicule = db.query(models.Vehicules).filter(models.Vehicules.id == vehicule_id).first()
    if db_vehicule is None:
        raise HTTPException(status_code=404, detail="Weapons not found")
    if vehicule.name is not None:
        db_vehicule.name = vehicule.name
    if vehicule.type is not None:
        db_vehicule.type = vehicule.type
    db.commit()
    return db_vehicule


# PUT function
def put_vehicule(db: Session, vehicule: schemas.VehiculeCreate, vehicule_id: int):
    db_vehicule = db.query(models.Vehicules).filter(models.Vehicules.id == vehicule_id).first()
    if db_vehicule is None:
        raise HTTPException(status_code=404, detail="Vehicule not found")
    db_vehicule.name = vehicule.name
    db_vehicule.type = vehicule.type
    db.commit()
    return db_vehicule
