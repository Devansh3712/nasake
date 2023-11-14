from __future__ import annotations

import bcrypt
from fastapi import status, APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from internal.error import *
from models.user import *
from routers.home import home
from schemas import UserLogin, UserSignUp

router = APIRouter(prefix="/auth")
templates = Jinja2Templates("templates")


@router.post("/signup")
async def signup(request: Request):
    form = dict(await request.form())
    user = UserSignUp(**form)  # type: ignore
    if read_user_by_email(user.email):
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": user_exists(user.email)}
        )
    if not create_user(user):
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": unable_to_make_user}
        )
    return RedirectResponse("/login", status.HTTP_303_SEE_OTHER)


@router.post("/login")
async def login(request: Request):
    form = dict(await request.form())
    user = UserLogin(**form)  # type: ignore
    db_user = read_user_by_email(user.email)
    if not db_user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": user_does_not_exist(user.email)},
        )
    result = bcrypt.checkpw(user.password.encode(), db_user.password.encode("utf-8"))
    if not result:
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": incorrect_password}
        )
    request.session["user_id"] = db_user.id
    return await home(request, db_user)
