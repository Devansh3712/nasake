from fastapi import status, APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from internal.error import Unauthorized
from internal.session import get_current_user
from models.user import User


router = APIRouter(prefix="/profile")
templates = Jinja2Templates("templates")


@router.get("/")
async def profile(request: Request, user: User | None = Depends(get_current_user)):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    return templates.TemplateResponse("profile.html", {"request": request})
