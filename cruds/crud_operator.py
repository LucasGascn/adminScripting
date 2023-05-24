from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET Function
def get_operators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operators).offset(skip).limit(limit).all()


# by ID
def get_operator(db: Session, operator_id: int):
    return db.query(models.Operators).filter(models.Operators.id == operator_id).first()


# by ID weapon
def get_operator_weapon(db: Session, weapon_id: int):
    return db.query(models.Operators).filter(models.Operators.weapon_id == weapon_id).all()


# by ID QG
def get_operator_qg(db: Session, qg_id: int):
    return db.query(models.Operators).filter(models.Operators.qg_id == qg_id).all()


# by ID of mission
def get_operator_mission(db: Session, mission_id: int):
    return db.query(models.Operators).filter(models.Operators.mission_id == mission_id).all()


# by name
def get_operator_name(db: Session, name: str):
    return db.query(models.Operators).filter(models.Operators.name == name).all()


# by nationality
def get_operator_nationality(db: Session, nationality: str):
    return db.query(models.Operators).filter(models.Operators.nationality == nationality).all()


# POST function
def create_operator(db: Session, operator: schemas.OperatorCreate):
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == operator.weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    db_qg = db.query(models.GQ).filter(models.GQ.id == operator.gq_id).first()
    if db_qg is None:
        raise HTTPException(status_code=404, detail="Quarter general not found")
    if operator.mission_id is not None:
        db_qg = db.query(models.Missions).filter(models.Missions.id == operator.mission_id).first()
        if db_qg is None:
            raise HTTPException(status_code=404, detail="Mission not found")
        db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, weapon_id=operator.weapon_id,
                                       mission_id=operator.mission_id, nationality=operator.nationality)
    else:
        db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, weapon_id=operator.weapon_id,
                                       nationality=operator.nationality)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


# DELETE function
def delete_operator(db: Session, operator_id: int):
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db.delete(db_operator)
    db.commit()
    return db_operator


# PATCH function
def patch_operator(operator_id: int, db: Session, operator: schemas.OperatorUpdate):
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    if operator.weapon_id is not None:
        db_operator.weapon_id = operator.weapon_id
    if operator.gq_id is not None:
        db_operator.gq_id = operator.gq_id
    if operator.name is not None:
        db_operator.name = operator.name
    if operator.nationality is not None:
        db_operator.nationality = operator.nationality
    if operator.mission_id is not None:
        db_operator.mission_id = operator.mission_id
    db.commit()
    return db_operator


# PUT function
def put_operator(db: Session, operator: schemas.OperatorCreate, operator_id: int):
    db_qg = db.query(models.GQ).filter(models.GQ.id == operator.gq_id).first()
    if db_qg is None:
        raise HTTPException(status_code=404, detail="Quarter General not found")
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == operator.weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    if operator.mission_id is not None:
        db_mission = db.query(models.Missions).filter(models.Missions.id == operator.mission_id).first()
        if db_mission is None:
            raise HTTPException(status_code=404, detail="Mission not found")
    db.commit()

    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db_operator.gq_id = operator.gq_id
    if operator.mission_id is not None:
        db_operator.mission_id = operator.mission_id
    db_operator.weapon_id = operator.weapon_id
    db_operator.name = operator.name
    db_operator.nationality = operator.nationality


# PUT function
def put_operator(db: Session, operator: schemas.OperatorCreate, operator_id: int):
    db_qg = db.query(models.GQ).filter(models.GQ.id == operator.gq_id).first()
    if db_qg is None:
        raise HTTPException(status_code=404, detail="Quarter General not found")
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == operator.weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    if operator.mission_id is not None:
        db_mission = db.query(models.Missions).filter(models.Missions.id == operator.mission_id).first()
        if db_mission is None:
            raise HTTPException(status_code=404, detail="Mission not found")

    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db_operator.gq_id = operator.gq_id
    if operator.mission_id is not None:
        db_operator.mission_id = operator.mission_id
    db_operator.weapon_id = operator.weapon_id
    db_operator.name = operator.name
    db_operator.nationality = operator.nationality

    db.commit()
    return db_operator
