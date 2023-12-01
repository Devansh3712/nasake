from datetime import datetime

from fastapi import status, APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from internal.analysis import emotion_analyzer
from internal.error import (
    DailyJournalCompleted,
    JournalEntryDoesNotExist,
    UnableToMakeJournalEntry,
    Unauthorized,
)
from internal.session import get_current_user
from models.journal import *
from models.schemas import JournalRequest
from models.user import User


router = APIRouter(prefix="/journal")
templates = Jinja2Templates("templates")
emotion_analysis = emotion_analyzer()


@router.get("/")
async def create_journal_entry(
    request: Request, user: User | None = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    recent_entry = read_last_entry(user.id)  # type: ignore
    if recent_entry:
        today = datetime.now()
        diff = today - recent_entry.created_at  # type: ignore
        if diff.days < 1:
            return templates.TemplateResponse(
                "error.html",
                {"request": request, "error": DailyJournalCompleted(today)},
                status.HTTP_400_BAD_REQUEST,
            )
    return templates.TemplateResponse("journal.html", {"request": request})


@router.post("/")
async def save_journal_entry(
    request: Request, user: User | None = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    form = dict(await request.form())
    form["user_id"] = request.session["user_id"]
    entry = JournalRequest(**form)  # type: ignore

    results = emotion_analysis(entry.body)[0]  # type: ignore
    emotions: dict[str, float] = {}
    for result in results:
        if result["score"] >= 0.01:
            emotions[result["label"]] = result["score"] * 100
    if not create_entry(entry, emotions):
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": UnableToMakeJournalEntry},
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    return RedirectResponse(f"/journal/{entry.id}", status.HTTP_303_SEE_OTHER)


@router.get("/{id}")
async def get_journal_entry(
    id: str, request: Request, user: User | None = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    entry = read_entry_by_id(id, user.id)  # type: ignore
    if not entry:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": JournalEntryDoesNotExist},
            status.HTTP_404_NOT_FOUND,
        )
    return templates.TemplateResponse(
        "analysis.html", {"request": request, "entry": entry}
    )
