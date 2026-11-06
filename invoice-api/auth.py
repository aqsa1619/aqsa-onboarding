import os
from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from db import get_db
from db_models import UserRow

load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"
bearer = HTTPBearer(auto_error=False)   # we send the 401 ourselves


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def create_token(user: UserRow) -> str:
    payload = {
        "sub": str(user.id),     # who the token belongs to
        "role": user.role,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=60),  # expiry
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def current_user(
    creds: HTTPAuthorizationCredentials | None = Depends(bearer),
    db: Session = Depends(get_db),
) -> UserRow:
    if creds is None:
        raise HTTPException(status_code=401, detail="Not logged in")
    try:
        payload = jwt.decode(creds.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError:       # fake, edited or expired token
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.get(UserRow, int(payload["sub"]))
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user