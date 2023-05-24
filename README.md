# adminScripting

# Projet-noSQL

Installation

DL fastAPI :pip install fastapi

need sqlalchemy for work.
DL sqlalchemy pip install sqlalchemy

need uvicorn for run the serve.
DL uvicorn : pip install "uvicorn[standard]"

run serve : uvicorn main:app --reload

File structure

appsql/
- database.py: Link with database; used by models.py .
- models.py: Class of the table in the database; used by schemas.py and use database.py .
- schemas.py: Class of the forms send, receive and use in API; use models.py .

cruds/
- crud_mission.py: Function interact with missions table, also interact with vehicules table for verification; used by routers.mission.py and use depedency.py .
- crud_operator.py: Function interact with operators table, also interact with weapons,general_quarter and missions tables for verification; used by routers.operator.py and use depedency.py .
- crud_qg.py: Function interact with general_quarter table; used by routers.qg.py and use depedency.py.
- crud_vehicule.py:  Function interact with vehicules table; used by routers.vehicule.py and use depedency.py.
- crud_weapon.py: Function interact with weapons table; used by routers.weapon.py and use depedency.py.

routers/
- mission.py: Receive HTML request and use function in crud_mission.py .
- operator.py: Receive HTML request and use function in crud_operator.py .
- qg.py: Receive HTML request and use function in crud_qg.py .
- vehicule.py: Receive HTML request and use function in crud_vehicule.py .
- weapon.py: Receive HTML request and use function in crud_weapon.py .

dependency.py: use appsql.database for open and close interaction with the database; use by all cruds/crud_- files .
main.py: Launch file who include all routers/ files and use appsql.database.py for create the database and the table if it is not initialise .
sql_app.db: The database create by main.py if is not initialise and use by all cruds/crud_- files .

List of HTML request

{Local Url used by Uvicorn}/docs#/