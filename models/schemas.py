from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import uuid4

import bcrypt
from pydantic import BaseModel, EmailStr


class UserSignUp(BaseModel):
    id: str = uuid4().hex
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()

    def hash_password(self) -> None:
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(self.password.encode(), salt)
        self.password = password_hash.decode()


class UserLogin(BaseModel):
    email: str
    password: str


class Error(BaseModel):
    code: int
    message: str
    detail: str


class JournalRequest(BaseModel):
    id: str = uuid4().hex
    user_id: str
    body: str
    created_at: datetime = datetime.now()


class ChatbotRequest(BaseModel):
    message: str
    timestamp: datetime = datetime.now()


class TestScore(BaseModel):
    score: tuple[int, int]
    result: str


class TestQuestion(BaseModel):
    question: str
    options: dict[str, int]


class Test(BaseModel):
    name: str
    prompt: str
    scores: list[TestScore]
    content: dict[int, TestQuestion]


class TestResult(BaseModel):
    id: str = uuid4().hex
    user_id: str
    name: str
    score: int
    created_at: datetime = datetime.now()


class Mode(Enum):
    online = "online"
    offline = "offline"
    both = "both"


class TherapistData(BaseModel):
    id: str = uuid4().hex
    name: str
    location: str
    mode: Mode
    contact: Optional[str] = None
    email: Optional[str] = None
    fees: int
