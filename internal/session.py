from fastapi import Request

from models.user import *


def get_current_user(request: Request) -> User | None:
    try:
        user_id = request.session["user_id"]
        return read_user_by_id(user_id)
    except:
        return None
