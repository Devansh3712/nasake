from contextlib import asynccontextmanager

from fastapi import status, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from config import settings
from internal.error import InternalServerError, PageNotFound
from models.database import Base, engine
from routers import (
    auth,
    chat,
    chat_room,
    disorders,
    journal,
    home,
    profile,
    search,
    spotify,
    tests,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(chat_room.router)
app.include_router(disorders.router)
app.include_router(journal.router)
app.include_router(home.router)
app.include_router(profile.router)
app.include_router(search.router)
app.include_router(spotify.router)
app.include_router(tests.router)

templates = Jinja2Templates("templates")


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def not_found(request: Request, exception: Exception):
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "error": PageNotFound,
            "image_path": "static/images/not_found.png",
        },
    )


@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def internal_server_error(request: Request, exception: Exception):
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "error": InternalServerError,
        },
    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/helplines", response_class=HTMLResponse)
async def helplines(request: Request):
    return templates.TemplateResponse("helplines.html", {"request": request})


@app.get("/tests", response_class=HTMLResponse)
async def tests_list(request: Request):
    return templates.TemplateResponse("tests.html", {"request": request})


@app.get("/bala")
async def depressed(request: Request):
    return RedirectResponse("https://www.youtube.com/shorts/-B19CcU3dhY")
