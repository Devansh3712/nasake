from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from models.database import Base, Session
from models.schemas import TherapistData, Mode


class TherapistEmail(Base):
    __tablename__ = "therapists_email"

    email = Column("email", String, primary_key=True)
    therapist_id = Column("therapist_id", String, ForeignKey("therapists.id"))


class TherapistContact(Base):
    __tablename__ = "therapists_contact"

    contact = Column("contact", String, primary_key=True)
    therapist_id = Column("therapist_id", String, ForeignKey("therapists.id"))


class Therapist(Base):
    __tablename__ = "therapists"

    id = Column("id", String, primary_key=True)
    name = Column("name", String, nullable=False)
    location = Column("location", String)
    mode = Column("mode", Enum(Mode), nullable=False)
    contact = relationship(TherapistContact, cascade="all,delete", lazy="selectin")
    email = relationship(TherapistEmail, cascade="all,delete", lazy="selectin")
    fees = Column("fees", Integer)


def create_therapist(data: TherapistData) -> bool:
    try:
        therapist_dict = data.model_dump()
        contact = therapist_dict["contact"]
        email = therapist_dict["email"]

        del therapist_dict["contact"]
        del therapist_dict["email"]
        therapist = Therapist(**therapist_dict)

        with Session() as session:
            session.add(therapist)
            if contact:
                session.add(
                    TherapistContact(therapist_id=therapist.id, contact=contact)
                )
            if email:
                session.add(TherapistEmail(therapist_id=therapist.id, email=email))
            session.commit()
        return True
    except:
        return False


def read_all_therapists() -> list[Therapist] | None:
    try:
        with Session() as session:
            result = session.query(Therapist).all()
        return result
    except:
        return None


def read_therapist_by_mode(mode: str) -> list[Therapist] | None:
    try:
        with Session() as session:
            result = session.query(Therapist).filter(Therapist.mode == mode).all()
        return result
    except:
        return None
