from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

"""
create models for database.
add primary_key and foreign_key for id
"""


class Operators(Base):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True, index=True)
    weapon_id = Column(Integer, ForeignKey("weapons.id"))
    gq_id = Column(Integer, ForeignKey("general_quarter.id"))
    mission_id = Column(Integer, ForeignKey("missions.id"))
    name = Column(String, index=True)
    nationality = Column(String, index=True)


class Weapons(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)

    operators = relationship("Operators", backref="weapons")


class Vehicules(Base):
    __tablename__ = "vehicules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)

    missions = relationship("Missions", backref="vehicules")


class GQ(Base):
    __tablename__ = "general_quarter"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)

    operators = relationship("Operators", backref="general_quarter")


class Missions(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    target = Column(String, index=True)
    vehicule_id = Column(Integer, ForeignKey("vehicules.id"))

    operators = relationship("Operators", backref="missions")
