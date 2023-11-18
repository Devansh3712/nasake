from typing import Callable

from fastapi import status

from models.schemas import Error

incorrect_password = Error(
    code=status.HTTP_401_UNAUTHORIZED,
    message="Incorrect Password",
    detail="The password you entered was incorrect. Try logging in again",
)

unauthorized = Error(
    code=status.HTTP_401_UNAUTHORIZED,
    message="User not authorized",
    detail="In order to access this page you need to be logged in",
)

unable_to_make_user = Error(
    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    message="Server Error",
    detail="Unable to create account. Try again later",
)

user_exists: Callable[[str], Error] = lambda email: Error(
    code=status.HTTP_403_FORBIDDEN,
    message="User exists",
    detail=f"Account with email {email} already exists",
)

user_does_not_exist: Callable[[str], Error] = lambda email: Error(
    code=status.HTTP_403_FORBIDDEN,
    message="User exists",
    detail=f"Account with email {email} does not exist",
)
