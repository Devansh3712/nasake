from functools import lru_cache

from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings


@lru_cache()
def get_engine() -> Engine:
    engine = create_engine(settings.POSTGRES_URI, echo=True)
    return engine


engine = get_engine()
Base = declarative_base()
Session = sessionmaker(bind=engine)
