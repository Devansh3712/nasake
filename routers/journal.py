from __future__ import annotations
from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from internal.error import unauthorized
from internal.session import get_current_user
from models.user import User

router = APIRouter(prefix="/journal")
templates = Jinja2Templates("templates")


@router.get("/journal")
async def create_journal_entry(
    request: Request, user: Optional[User] = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": unauthorized}
        )


@router.post("/journal")
async def save_journal_entry(
    request: Request, user: Optional[User] = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": unauthorized}
        )
