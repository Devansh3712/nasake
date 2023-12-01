from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/disorders")
templates = Jinja2Templates("templates")


@router.get("/")
async def illnesses(request: Request):
    return templates.TemplateResponse("disorders.html", {"request": request})


@router.get("/self-harm")
async def self_harm(request: Request):
    return templates.TemplateResponse("selfHarm.html", {"request": request})


@router.get("/psychosis")
async def psychosis(request: Request):
    return templates.TemplateResponse("psychosis.html", {"request": request})


@router.get("/anxiety")
async def anxiety(request: Request):
    return templates.TemplateResponse("anxiety.html", {"request": request})


@router.get("/depression")
async def depression(request: Request):
    return templates.TemplateResponse("depression.html", {"request": request})
