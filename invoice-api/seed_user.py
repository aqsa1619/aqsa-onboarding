from auth import hash_password
from db import Base, SessionLocal, engine
from db_models import UserRow

Base.metadata.create_all(engine)
db = SessionLocal()

if not db.query(UserRow).filter_by(email="admin@test.com").first():
    db.add(UserRow(
        email="admin@test.com",
        password_hash=hash_password("admin123"),
        role="admin",
    ))
    db.commit()
    print("Created admin@test.com")
else:
    print("User already exists")

db.close()