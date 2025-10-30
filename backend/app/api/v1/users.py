# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/")
# def get_users():
#     return {"users": []}

# app/api/v1/users.py


from fastapi import APIRouter, Depends, HTTPException
from app.models.sqlalchemy_models import User
from app.schemas.pydantic_schemas import UserOut
from app.core.security import get_current_user  # We’ll add this below

router = APIRouter()


@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

