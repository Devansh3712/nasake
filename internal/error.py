from datetime import datetime
from typing import Callable

from fastapi import status

from models.schemas import Error

PageNotFound = Error(
    code=status.HTTP_404_NOT_FOUND,
    message="Page Not Found",
    detail="The page you're trying to find does not exist",
)

InternalServerError = Error(
    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    message="Internal Server Error",
    detail="There is a problem with the server, try again later",
)

IncorrectPassword = Error(
    code=status.HTTP_401_UNAUTHORIZED,
    message="Incorrect Password",
    detail="The password you entered was incorrect. Try logging in again",
)

Unauthorized = Error(
    code=status.HTTP_401_UNAUTHORIZED,
    message="User not authorized",
    detail="In order to access this page you need to be logged in",
)

UnableToMakeUser = Error(
    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    message="Server Error",
    detail="Unable to create account. Try again later",
)

UserExists: Callable[[str], Error] = lambda email: Error(
    code=status.HTTP_403_FORBIDDEN,
    message="User exists",
    detail=f"Account with email {email} already exists",
)

UserDoesNotExist: Callable[[str], Error] = lambda email: Error(
    code=status.HTTP_403_FORBIDDEN,
    message="User exists",
    detail=f"Account with email {email} does not exist",
)

UnableToMakeJournalEntry = Error(
    code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    message="Server Error",
    detail="Unable to make a journal entry. Try again later",
)

JournalEntryDoesNotExist = Error(
    code=status.HTTP_404_NOT_FOUND,
    message="Journal entry does not exist",
    detail="The journal entry you're trying to find doesn't exist",
)

DailyJournalCompleted: Callable[[datetime], Error] = lambda date: Error(
    code=status.HTTP_400_BAD_REQUEST,
    message="Daily journal entry written",
    detail=f"Journal for {date.strftime('%d %B, %Y')} has already been written.\
        You can only write one entry per day, try again tomorrow",
)

TestScoreDoesNotExist = Error(
    code=status.HTTP_404_NOT_FOUND,
    message="Test score does not exist",
    detail="The test score you're trying to find doesn't exist",
)
