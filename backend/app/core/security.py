from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config import settings
from app.db.database import SessionLocal
from app.models.sqlalchemy_models import User

import hashlib
import bcrypt # Import bcrypt directly
from passlib.context import CryptContext # Keep for other schemes if needed, but not for bcrypt here

# Password hashing context (we'll use bcrypt directly)
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # No longer needed for bcrypt

# Token configuration for FastAPI security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# -------------------------------
# Password utilities
# -------------------------------
def get_password_hash(password: str) -> str:
    # Pre-hash the password to avoid bcrypt 72-byte limit
    sha256_hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    # Hash the pre-hashed password using bcrypt
    hashed_bytes = bcrypt.hashpw(sha256_hashed.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Pre-hash the plain password for comparison
    sha256_hashed = hashlib.sha256(plain_password.encode('utf-8')).hexdigest()
    # Verify the pre-hashed password against the stored hash
    return bcrypt.checkpw(sha256_hashed.encode('utf-8'), hashed_password.encode('utf-8'))

# -------------------------------
# JWT token creation
# -------------------------------
def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=expires_delta or getattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES", 120)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

# -------------------------------
# Get Current User (JWT validation)
# -------------------------------
def get_current_user(token: str = Depends(oauth2_scheme)):
    db = SessionLocal()
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    finally:
        db.close()

