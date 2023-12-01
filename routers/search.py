from typing import Literal

from fastapi import status, APIRouter, Request
from fastapi.templating import Jinja2Templates

from models.therapist import read_all_therapists, read_therapist_by_mode

router = APIRouter(prefix="/search")
templates = Jinja2Templates("templates")
modes = Literal["all", "offline", "online", "both"]


@router.get("/")
async def search(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@router.get("/therapist")
async def get_therapists(request: Request, mode: modes):
    therapists = ...
    match mode:
        case "all":
            therapists = read_all_therapists()
        case _:
            therapists = read_therapist_by_mode(mode)
    return therapists
