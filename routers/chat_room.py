import json
from uuid import uuid4

from better_profanity import profanity
from fastapi import (
    status,
    APIRouter,
    Depends,
    Request,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from internal.error import Unauthorized
from internal.session import get_current_user
from models.user import User


router = APIRouter(prefix="/chat-room")
templates = Jinja2Templates("templates")


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: dict[str, WebSocket] = {}
        self.user_warnings: dict[str, int] = {}

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        user_id = uuid4().hex
        self.active_connections[user_id] = websocket
        self.user_warnings[user_id] = 0

    async def send_message(self, ws: WebSocket, message: str) -> None:
        await ws.send_text(message)

    async def send_message_to_all(self, message: str) -> None:
        for connection in self.active_connections.values():
            await connection.send_text(message)

    def find_connection_id(self, websocket: WebSocket):
        return next(
            id for id, conn in self.active_connections.items() if conn == websocket
        )

    async def broadcast(self, webSocket: WebSocket, data: str) -> None:
        decoded_data = json.loads(data)
        message = decoded_data["message"]
        username = decoded_data["username"]

        if profanity.contains_profanity(message):
            user_id = self.find_connection_id(webSocket)
            self.user_warnings[user_id] += 1
            warnings = self.user_warnings[user_id]
            await self.send_message(
                webSocket,
                json.dumps(
                    {
                        "isMe": True,
                        "data": f"Warning {warnings}/3: Profanity not allowed.",
                        "username": "System",
                    }
                ),
            )
            if warnings == 3:
                await self.disconnect(webSocket)
                return

            message = "**Content Removed**"

        for connection_id, connection in self.active_connections.items():
            is_me = connection == webSocket
            await connection.send_text(
                json.dumps({"isMe": is_me, "data": message, "username": username})
            )

    async def disconnect(self, websocket: WebSocket) -> None:
        user_id = self.find_connection_id(websocket)
        del self.active_connections[user_id]
        del self.user_warnings[user_id]

        await websocket.close()


connection_manager = ConnectionManager()


@router.get("/")
async def get_room(request: Request, user: User | None = Depends(get_current_user)):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    return templates.TemplateResponse("chat_room.html", {"request": request})


@router.websocket("/message")
async def ws_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await connection_manager.broadcast(websocket, data)
    except WebSocketDisconnect:
        await connection_manager.disconnect(websocket)
        return RedirectResponse("/home")
