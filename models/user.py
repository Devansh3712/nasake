from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from models.database import Base, Session
from models.journal import Journal as _
from models.schemas import UserSignUp


class User(Base):
    __tablename__ = "users"

    id = Column("id", String, primary_key=True)
    first_name = Column("first_name", String, nullable=False)
    last_name = Column("last_name", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False)
    journals = relationship("Journal")


def create_user(data: UserSignUp) -> bool:
    try:
        data.hash_password()
        user = User(**data.model_dump())
        with Session() as session:
            session.add(user)
            session.commit()
        return True
    except:
        return False


def read_user_by_email(email: str) -> User | None:
    try:
        with Session() as session:
            result = session.query(User).filter(User.email == email).one()
        return result
    except:
        return None


def read_user_by_id(id: str) -> User | None:
    try:
        with Session() as session:
            result = session.query(User).filter(User.id == id).one()
        return result
    except:
        return None
