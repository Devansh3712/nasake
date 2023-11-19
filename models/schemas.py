from datetime import datetime
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
