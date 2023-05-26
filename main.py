from fastapi import FastAPI, Request
from routers import mission, operator, qg, vehicule, weapon
from appsql import models
from appsql.database import engine
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import Point
import time
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

bucket = "projectone"
org = "project"
token = "BKjW5CQlPW-x0xg8N2rRXRaFLlEMPaPMPOCXRfMXcUf9FJqTt3oWjxGeaozalW3IG2nitrvtNc7mmN1vhdh_RA=="
# Store the URL of your InfluxDB instance
url="http://192.168.64.17:8086"


client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    point = (
        Point.measurement("back")
        .tag("Type", "Request")
        .tag("Route", request.url)
        .tag("Agent", "VM-Projet")
        .field("ProcessTime", process_time)
    )

    write_api.write(bucket=bucket, org=org, record=point)

    return response


app.include_router(mission.router)
app.include_router(operator.router)
app.include_router(qg.router)
app.include_router(vehicule.router)
app.include_router(weapon.router)