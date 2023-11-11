from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from config import settings
from models.database import Base, engine
from routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)


@app.get("/")
async def index():
    ...
