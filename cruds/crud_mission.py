from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET function
def get_mission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Missions).offset(skip).limit(limit).all()


# Create function
def create_mission(db: Session, mission: schemas.MissionCreate):
    db_vehicule = db.query(models.Vehicules).filter(models.Vehicules.id == mission.vehicule_id).first()
    if db_vehicule is None and mission.vehicule_id is not None:
        raise HTTPException(status_code=404, detail="This vehicule don't exist")
    if mission.vehicule_id is None:
        db_mission = models.Missions(target=mission.target)
    else:
        db_mission = models.Missions(target=mission.target, vehicule_id=mission.vehicule_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


# DELETE function
def delete_mission(db: Session, mission_id: int):
    db_mission = db.query(models.Missions).filter(models.Missions.id == mission_id).first()
    if db_mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    db.delete(db_mission)
    db.commit()
    return db_mission


# PATCH function
def patch_mission(mission_id: int, db: Session, mission: schemas.MissionUpdate):
    db_mission = db.query(models.Missions).filter(models.Missions.id == mission_id).first()
    if db_mission is None:
        raise HTTPException(status_code=404, detail="Weapons not found")
    if mission.target is not None:
        db_mission.target = mission.target
    if mission.vehicule_id is not None:
        db_mission.vehicule_id = mission.vehicule_id
    db.commit()
    return db_mission


# PUT function
def put_mission(db: Session, mission: schemas.MissionCreate, mission_id: int):
    db_mission = db.query(models.Missions).filter(models.Missions.id == mission_id).first()
    if db_mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    db_vehicule = db.query(models.Vehicules).filter(models.Vehicules.id == mission.vehicule_id).first()
    if db_vehicule is None:
        raise HTTPException(status_code=404, detail="Vehicule not found")
    db_mission.target = mission.target
    db_mission.vehicule_id = mission.vehicule_id
    db.commit()
    return db_mission
