from datetime import datetime

from fastapi import status, APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from internal.error import TestScoreDoesNotExist, Unauthorized
from internal.session import get_current_user
from internal.tests.adhd import adhd_test
from internal.tests.anxiety import anxiety_test
from internal.tests.bipolar import bipolar_test
from internal.tests.depression import depression_test
from internal.tests.psychosis import psychosis_test
from internal.tests.ptsd import ptsd_test
from internal.tests.youth import youth_test
from models.schemas import TestResult
from models.test import *
from models.user import User


router = APIRouter(prefix="/tests")
templates = Jinja2Templates("templates")

tests = {
    "depression-test": depression_test,
    "anxiety-test": anxiety_test,
    "adhd-test": adhd_test,
    "bipolar-test": bipolar_test,
    "psychosis-test": psychosis_test,
    "ptsd-test": ptsd_test,
    "youth-test": youth_test,
}


@router.get("/{name}")
async def render_test(name: str, request: Request):
    if name not in tests.keys():
        return templates.TemplateResponse(
            "error.html", {"request": request}, status.HTTP_404_NOT_FOUND
        )
    return templates.TemplateResponse(
        "test.html", {"request": request, "name": name, "test": tests[name]}
    )


@router.post("/{name}")
async def score_test(
    name: str, request: Request, user: User | None = Depends(get_current_user)
):
    if name not in tests.keys():
        return templates.TemplateResponse(
            "error.html", {"request": request}, status.HTTP_404_NOT_FOUND
        )
    if name not in tests.keys():
        return templates.TemplateResponse(
            "error.html", {"request": request}, status.HTTP_404_NOT_FOUND
        )
    form = await request.form()
    test = tests[name]
    score = 0
    for _, value in form.items():
        score += int(value)  # type: ignore
    result = ...
    for score_range in test.scores:
        if score_range.score[0] <= score and score_range.score[1] >= score:
            result = score_range.result
            break
    if user:
        create_test_score(TestResult(user_id=user.id, name=name, score=score))  # type: ignore
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "test": test,
            "score": score,
            "result": result,
            "date": datetime.now(),
        },
    )


@router.get("/score/{id}")
async def get_test_score(
    id: str, request: Request, user: User | None = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    test_result = read_score_by_id(id, user.id)  # type: ignore
    if not test_result:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": TestScoreDoesNotExist},
            status.HTTP_404_NOT_FOUND,
        )
    test = tests[test_result.name]  # type: ignore
    score = test_result.score
    result = ...
    for score_range in test.scores:
        if score_range.score[0] <= score and score_range.score[1] >= score:  # type: ignore
            result = score_range.result
            break
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "test": test,
            "score": score,
            "result": result,
            "date": test_result.created_at,
        },
    )
