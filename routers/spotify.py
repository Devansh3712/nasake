import httpx
from fastapi import status, APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from internal.error import Unauthorized
from internal.session import get_current_user
from internal.spotify import (
    create_playlist,
    create_spotify_api_instance,
    get_top_artists,
    get_top_tracks,
    select_tracks,
    spotify_oauth,
)
from models.user import User


router = APIRouter(prefix="/spotify")
templates = Jinja2Templates("templates")


@router.get("/")
async def authorize(
    request: Request, mood: float, user: User | None = Depends(get_current_user)
):
    if not user:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": Unauthorized},
            status.HTTP_401_UNAUTHORIZED,
        )
    auth_url = spotify_oauth.get_authorize_url()
    request.session["mood"] = mood
    return RedirectResponse(auth_url)


@router.get("/callback")
async def callback(
    request: Request, code: str, user: User | None = Depends(get_current_user)
):
    data = spotify_oauth.get_access_token(code, check_cache=False)
    access_token = data["access_token"]
    spotify = create_spotify_api_instance(access_token)

    mood = float(request.session["mood"])
    top_artists = get_top_artists(spotify)
    top_tracks = get_top_tracks(spotify, top_artists)
    selected_tracks = select_tracks(mood, spotify, top_tracks)
    playlist_id = create_playlist(mood, spotify, selected_tracks)

    spotify_url = f"https://open.spotify.com/playlist/{playlist_id}"
    response = httpx.get(f"https://open.spotify.com/oembed?url={spotify_url}")
    if response.status_code != 200:
        return RedirectResponse(spotify_url)

    embed = response.json()["html"]
    return templates.TemplateResponse(
        "playlist.html", {"request": request, "embed": embed}
    )
