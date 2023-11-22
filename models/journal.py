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


def read_entry_by_id(id: str) -> Journal | None:
    try:
        with Session() as session:
            result = session.query(Journal).filter(Journal.id == id).one()
        return result
    except:
        return None


def read_recent_entry() -> Journal | None:
    try:
        with Session() as session:
            result = session.query(Journal).order_by(desc(Journal.created_at)).first()
        return result
    except:
        return None
