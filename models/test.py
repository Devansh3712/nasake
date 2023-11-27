from sqlalchemy import desc, Column, DateTime, ForeignKey, String, Integer

from models.database import Base, Session
from models.schemas import TestResult


class Test(Base):
    __tablename__ = "tests"

    id = Column("id", String, primary_key=True)
    user_id = Column("user_id", String, ForeignKey("users.id"))
    name = Column("name", String, nullable=False)
    score = Column("score", Integer, nullable=False)
    created_at = Column("created_at", DateTime, nullable=False)


def create_test_score(result: TestResult) -> bool:
    try:
        test = Test(**result.model_dump())
        with Session() as session:
            session.add(test)
            session.commit()
        return True
    except:
        return False


def read_score_by_id(id: str, user_id: str) -> Test | None:
    try:
        with Session() as session:
            result = (
                session.query(Test).filter(Test.id == id, Test.user_id == user_id).one()
            )
        return result
    except:
        return None


def read_recent_scores(user_id: str, count: int = 5) -> list[Test] | None:
    try:
        with Session() as session:
            result = (
                session.query(Test)
                .filter(Test.user_id == user_id)
                .order_by(desc(Test.created_at))
                .limit(count)
            )
        return result.all()
    except:
        return None
