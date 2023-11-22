from fastapi import status, APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from openai import Client

from config import settings
from internal.error import Unauthorized
from internal.session import get_current_user
from models.schemas import ChatbotRequest
from models.user import User

router = APIRouter(prefix="/chat")
templates = Jinja2Templates("templates")


client = Client(api_key=settings.OPENAI_API_KEY)
messages = [
    {
        "role": "system",
        "content": "Your are tsuki, an assistant who will listen to people vent out whatever they want to. \
            Sympathise with them and give them some valuable insights that can be useful in their situation.",
    }
]


@router.get("/")
async def chat_page(request: Request, user: User | None = Depends(get_current_user)):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    return templates.TemplateResponse("chat.html", {"request": request})


@router.post("/")
async def chatbot(request: ChatbotRequest):
    messages.append({"role": "user", "content": request.message})
    response = client.chat.completions.create(model="gpt-3.5-turbo-16k-0613", messages=messages)  # type: ignore
    chat_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_response})  # type: ignore
    return chat_response
