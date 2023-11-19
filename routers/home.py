import httpx
from fastapi import status, APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from internal.error import Unauthorized
from internal.session import get_current_user
from models.user import User

router = APIRouter(prefix="/home")
templates = Jinja2Templates("templates")


@router.get("/")
async def home(request: Request, user: User | None = Depends(get_current_user)):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    response = httpx.get("https://zenquotes.io/api/random")
    data = response.json()
    return templates.TemplateResponse(
        "home.html", {"request": request, "user": user, "quote": data[0]["q"]}
    )
