from functools import lru_cache

from sqlalchemy import create_engine, Engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


@lru_cache()
def get_engine() -> Engine:
    url = URL.create(
        "postgresql",
        username=settings.POSTGRES_USERNAME,
        password=settings.POSTGRES_PASSWORD,
        host=settings.POSTGRES_HOST,
        database=settings.POSTGRES_DATABASE,
    )
    engine = create_engine(url, echo=True)
    return engine


engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
