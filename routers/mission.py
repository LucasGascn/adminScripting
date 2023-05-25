from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_mission

router = APIRouter()


# POST Function
@router.post("/missions/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud_mission.create_mission(db=db, mission=mission)


# GET Function
@router.get("/missions/", response_model=List[schemas.Mission])
def read_mission(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mission = crud_mission.get_mission(db, skip=skip, limit=limit)
    return mission


# DELETE Function
@router.delete("/missions/{mission_id}")
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    db_mission = crud_mission.delete_mission(db=db, mission_id=mission_id)
    return "Mission erased"


# PATCH Function
@router.patch("/missions/{mission_id}", response_model=schemas.Mission)
def update_mission(mission_id: int, mission: schemas.MissionUpdate, db: Session = Depends(get_db)):
    db_mission = crud_mission.patch_mission(db=db, mission_id=mission_id, mission=mission)
    return db_mission


# PUT Function
@router.put("/missions/{mission_id}", response_model=schemas.Mission)
def change_mission(mission: schemas.MissionCreate, mission_id: int, db: Session = Depends(get_db)):
    db_mission = crud_mission.put_mission(db, mission_id=mission_id, mission=mission)
    return db_mission
