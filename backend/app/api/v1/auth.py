# from fastapi import APIRouter

# router = APIRouter()

# @router.post("/login")
# def login():
#     return {"message": "Login endpoint"}

# @router.post("/register")
# def register():
#     return {"message": "Register endpoint"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.sqlalchemy_models import User
from app.schemas.pydantic_schemas import UserCreate, UserOut, UserLogin
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_pw = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        print(f"Database error during user registration: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    print("user scemaa", user)
    db_user = db.query(User).filter(User.email == user.email).first()
    # db_user = db.query(User).all()
    print("db_user", db_user)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}