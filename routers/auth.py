from __future__ import annotations

import bcrypt
from fastapi import status, APIRouter, HTTPException, Request

from models.user import *
from schemas import UserLogin, UserResponse, UserSignUp

router = APIRouter(prefix="/auth")


@router.post("/")
async def signup(request: Request, user: UserSignUp):
    if read_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Account with email {user.email} already exists",
        )
    if not create_user(user):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create account",
        )
    request.session["user_id"] = user.id
    return UserResponse(**user.model_dump())


@router.get("/")
async def login(request: Request, user: UserLogin):
    db_user = read_user_by_email(user.email)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Account with email {user.email} does not exist",
        )
    result = bcrypt.checkpw(user.password.encode(), db_user.password.encode("utf-8"))
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )
    request.session["user_id"] = db_user.id
    return UserResponse.model_validate(db_user)


def get_current_user(request: Request) -> User | None:
    try:
        user_id = request.session["user_id"]
        return read_user_by_id(user_id)
    except:
        return None
