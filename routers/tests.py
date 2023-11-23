from fastapi import status, APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from internal.error import Unauthorized
from internal.session import get_current_user
from internal.tests.adhd import adhd_test
from internal.tests.anxiety import anxiety_test
from internal.tests.bipolar import bipolar_test
from internal.tests.depression import depression_test
from internal.tests.psychosis import psychosis_test
from internal.tests.ptsd import ptsd_test
from internal.tests.youth import youth_test
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


@router.get("/")
async def tests_list(request: Request, user: User | None = Depends(get_current_user)):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    return templates.TemplateResponse("tests.html", {"request": request})


@router.get("/{name}")
async def render_test(
    name: str, request: Request, user: User | None = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
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
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    if name not in tests.keys():
        return templates.TemplateResponse(
            "error.html", {"request": request}, status.HTTP_404_NOT_FOUND
        )
    form = await request.form()
