import bcrypt
from fastapi import status, APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from internal.error import *
from internal.session import get_current_user
from models.user import *
from models.schemas import UserLogin, UserSignUp

router = APIRouter(prefix="/auth")
templates = Jinja2Templates("templates")


@router.post("/signup")
async def signup(request: Request):
    form = dict(await request.form())
    user = UserSignUp(**form)  # type: ignore
    if read_user_by_email(user.email):
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": UserExists(user.email)},
            status.HTTP_403_FORBIDDEN,
        )
    if not create_user(user):
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": UnableToMakeUser},
            status.HTTP_500_INTERNAL_SERVER_ERROR,
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
            {"request": request, "error": UserDoesNotExist(user.email)},
            status.HTTP_403_FORBIDDEN,
        )
    result = bcrypt.checkpw(user.password.encode(), db_user.password.encode("utf-8"))
    if not result:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": IncorrectPassword},
            status.HTTP_401_UNAUTHORIZED,
        )
    # Create a user session
    request.session["user_id"] = db_user.id
    return RedirectResponse("/home", status.HTTP_303_SEE_OTHER)


@router.get("/logout")
async def logout(request: Request, user: User | None = Depends(get_current_user)):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    # Delete a user session
    del request.session["user_id"]
    return templates.TemplateResponse("message.html", {"request": request})
