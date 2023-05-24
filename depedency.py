from appsql.database import SessionLocal


# Liaison BDD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
