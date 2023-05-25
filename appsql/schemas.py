from pydantic import BaseModel


# OPERATOR SCHEMAS
class OperatorBase(BaseModel):
    pass


class OperatorUpdate(OperatorBase):
    weapon_id: int or None = None
    gq_id: int or None = None
    mission_id: int or None = None
    name: str or None = None
    nationality: str or None = None


class OperatorCreate(OperatorBase):
    weapon_id: int
    gq_id: int
    mission_id: int or None = None
    name: str
    nationality: str


class Operator(OperatorBase):
    id: int
    weapon_id: int
    gq_id: int or None
    mission_id: int or None
    name: str
    nationality: str

    class Config:
        orm_mode = True


# WEAPON SCHEMAS

class WeaponBase(BaseModel):
    pass


class WeaponCreate(WeaponBase):
    id: int
    name: str
    type: str


class WeaponUpdate(WeaponBase):
    name: str or None = None
    type: str or None = None


class Weapon(WeaponBase):
    id: int
    name: str
    type: str

    class Config:
        orm_mode = True


# QG SCHEMAS

class QGBase(BaseModel):
    country: str


class QGCreate(QGBase):
    pass


class QG(QGBase):
    id: int
    country: str

    class Config:
        orm_mode = True


# MISSION SCHEMAS
class MissionBase(BaseModel):
    pass


class MissionCreate(MissionBase):
    target: str
    vehicule_id: int or None


class MissionUpdate(MissionBase):
    target: str or None = None
    vehicule_id: int or None = None


class Mission(MissionBase):
    id: int
    target: str
    vehicule_id: int or None

    class Config:
        orm_mode = True


# VEHICULE SCHEMAS
class VehiculeBase(BaseModel):
   pass


class VehiculeCreate(VehiculeBase):
    name: str
    type: str


class VehiculeUpdate(VehiculeBase):
    name: str or None = None
    type: str or None = None


class Vehicule(VehiculeBase):
    id: int
    name: str
    type: str

    class Config:
        orm_mode = True
