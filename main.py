from fastapi import FastAPI
from routers import mission, operator, qg, vehicule, weapon
from appsql import models
from appsql.database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(mission.router)
app.include_router(operator.router)
app.include_router(qg.router)
app.include_router(vehicule.router)
app.include_router(weapon.router)


