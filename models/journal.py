from sqlalchemy import desc, Column, DateTime, ForeignKey, JSON, String, Text

from models.database import Base, Session
from models.schemas import JournalRequest


class Journal(Base):
    __tablename__ = "journals"

    id = Column("id", String, primary_key=True)
    user_id = Column("user_id", String, ForeignKey("users.id"))
    body = Column("body", Text, nullable=False)
    emotions = Column("emotions", JSON, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False)


def create_entry(data: JournalRequest, emotions: dict[str, float]) -> bool:
    try:
        journal = Journal(**data.model_dump(), emotions=emotions)
        with Session() as session:
            session.add(journal)
            session.commit()
        return True
    except:
        return False


def read_entry_by_id(id: str, user_id: str) -> Journal | None:
    try:
        with Session() as session:
            result = (
                session.query(Journal)
                .filter(Journal.id == id, Journal.user_id == user_id)
                .one()
            )
        return result
    except:
        return None


def read_last_entry(user_id: str) -> Journal | None:
    try:
        with Session() as session:
            result = (
                session.query(Journal)
                .filter(Journal.user_id == user_id)
                .order_by(desc(Journal.created_at))
                .first()
            )
        return result
    except:
        return None


def read_recent_entries(user_id: str, count: int = 5) -> list[Journal] | None:
    try:
        with Session() as session:
            result = (
                session.query(Journal)
                .filter(Journal.user_id == user_id)
                .order_by(desc(Journal.created_at))
                .limit(count)
            )
        return result.all()
    except:
        return None
