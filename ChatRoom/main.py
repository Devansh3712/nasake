from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from dataclasses import dataclass
from typing import Dict
import uuid
import json
from fastapi.staticfiles import StaticFiles
from better_profanity import profanity

templates = Jinja2Templates(directory="templates")

@dataclass
class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: Dict[str, WebSocket] = {}
        self.user_warnings: Dict[str, int] = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        user_id = str(uuid.uuid4())
        self.active_connections[user_id] = websocket
        self.user_warnings[user_id] = 0

        # Generate a user-friendly name or message
        user_message = f"A new user has joined the chat room!"

        # Send a system message to all active connections
        await self.send_message_to_all(json.dumps({"isMe": False, "data": user_message, "username": "System"}))

        await self.send_message(websocket, json.dumps({"isMe": True, "data": "Welcome to the chat room!", "username": "System"}))

    async def send_message(self, ws: WebSocket, message: str):
        await ws.send_text(message)

    async def send_message_to_all(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

    def find_connection_id(self, websocket: WebSocket):
        return next(id for id, conn in self.active_connections.items() if conn == websocket)

    async def broadcast(self, webSocket: WebSocket, data: str):
        decoded_data = json.loads(data)
        message = decoded_data['message']
        username = decoded_data['username']

        # Check message for profanity
        if profanity.contains_profanity(message):
            user_id = self.find_connection_id(webSocket)
            self.user_warnings[user_id] += 1
            warnings = self.user_warnings[user_id]
            await self.send_message(webSocket, json.dumps({"isMe": True, "data": f"Warning {warnings}/3: Profanity not allowed.", "username": "System"}))
            if warnings >= 3:
                await self.disconnect(webSocket)
                return

            # Replace profane message with a warning message
            message = f"**Content Removed**"

        for connection_id, connection in self.active_connections.items():
            is_me = connection == webSocket
            await connection.send_text(json.dumps({"isMe": is_me, "data": message, "username": username}))

    async def disconnect(self, websocket: WebSocket):
        user_id = self.find_connection_id(websocket)
        del self.active_connections[user_id]
        del self.user_warnings[user_id]

        # Notify all active connections about user disconnection
        await self.send_message_to_all(json.dumps({"isMe": False, "data": "A user has left the chat room.", "username": "System"}))

        # Notify user about disconnection due to profanity
        await self.send_message(websocket, json.dumps({"isMe": True, "data": "You have been removed from the chat room due to profanity.", "username": "System"}))

        await websocket.close()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
connection_manager = ConnectionManager()

@app.get("/", response_class=HTMLResponse)
def get_room(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/message")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await connection_manager.broadcast(websocket, data)
    except WebSocketDisconnect:
        await connection_manager.disconnect(websocket)
        return RedirectResponse("/")

@app.get("/join", response_class=HTMLResponse)
def get_room(request: Request):
    return templates.TemplateResponse("room.html", {"request": request})
