import random

import spotipy
from spotipy import oauth2

from config import settings


scopes = [
    "user-library-read",
    "user-top-read",
    "user-follow-read",
    "playlist-modify-public",
]
spotify_oauth = oauth2.SpotifyOAuth(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET,
    redirect_uri=settings.SPOTIFY_REDIRECT_URI,
    scope=" ".join(scopes),
)

moods = {
    "admiration": 0.8,
    "amusement": 0.9,
    "anger": 0.3,
    "annoyance": 0.4,
    "approval": 0.7,
    "caring": 0.8,
    "confusion": 0.4,
    "curiosity": 0.6,
    "desire": 0.7,
    "disappointment": 0.3,
    "disapproval": 0.3,
    "disgust": 0.2,
    "embarrassment": 0.4,
    "excitement": 1,
    "fear": 0.2,
    "gratitude": 0.8,
    "grief": 0.1,
    "joy": 1,
    "love": 0.9,
    "nervousness": 0.3,
    "optimism": 0.8,
    "pride": 0.8,
    "realization": 0.7,
    "relief": 0.7,
    "remorse": 0.2,
    "sadness": 0.1,
    "surprise": 0.8,
    "neutral": 0.5,
}


def calculate_mood(emotions: dict[str, float]) -> float:
    mood = 0.0
    for emotion in emotions:
        mood += moods[emotion] * emotions[emotion]
    return mood / 100


def create_spotify_api_instance(access_token: str) -> spotipy.Spotify:
    return spotipy.Spotify(access_token)


def get_top_artists(sp: spotipy.Spotify) -> list[str]:
    top_artists: set[str] = set()
    ranges = ["short_term", "medium_term", "long_term"]

    for _range in ranges:
        data = sp.current_user_top_artists(limit=50, time_range=_range)
        for artist in data["items"]:
            top_artists.add(artist["uri"])

    followed_artists = sp.current_user_followed_artists(limit=50)
    for artist in followed_artists["artists"]["items"]:
        top_artists.add(artist["uri"])

    return list(top_artists)


def get_top_tracks(sp: spotipy.Spotify, top_artists: list[str]) -> list[str]:
    top_tracks: list[str] = []
    for artist in top_artists:
        data = sp.artist_top_tracks(artist, country="IN")
        for track in data["tracks"]:
            top_tracks.append(track["uri"])

    return top_tracks


def select_tracks(mood: float, sp: spotipy.Spotify, top_tracks: list[str]):
    tracks = []
    random.shuffle(top_tracks)

    for i in range(0, len(top_tracks), 50):
        data = sp.audio_features(top_tracks[i : i + 50])
        for track in data:
            valence = track["valence"]
            danceability = track["danceability"]
            energy = track["energy"]
            uri = track["uri"]

            if mood < 0.10:
                if (
                    (0 <= valence <= (mood + 0.15))
                    and danceability <= (mood * 8)
                    and energy <= (mood * 10)
                ):
                    tracks.append(uri)
            elif 0.10 <= mood < 0.25:
                if (
                    ((mood - 0.075) <= valence <= (mood + 0.075))
                    and danceability <= (mood * 4)
                    and energy <= (mood * 5)
                ):
                    tracks.append(uri)
            elif 0.25 <= mood < 0.50:
                if (
                    ((mood - 0.05) <= valence <= (mood + 0.05))
                    and danceability <= (mood * 1.75)
                    and energy <= (mood * 1.75)
                ):
                    tracks.append(uri)
            elif 0.50 <= mood < 0.75:
                if (
                    ((mood - 0.075) <= valence <= (mood + 0.075))
                    and danceability >= (mood / 2.5)
                    and energy >= (mood / 2)
                ):
                    tracks.append(uri)
            elif 0.75 <= mood < 0.90:
                if (
                    ((mood - 0.075) <= valence <= (mood + 0.075))
                    and danceability >= (mood / 2)
                    and energy >= (mood / 1.75)
                ):
                    tracks.append(uri)
            else:
                if (
                    ((mood - 0.15) <= valence <= 1)
                    and danceability >= (mood / 1.75)
                    and energy >= (mood / 1.5)
                ):
                    tracks.append(uri)

    return tracks


def create_playlist(mood: float, sp: spotipy.Spotify, tracks: list[str]) -> str:
    user_data = sp.current_user()
    user_id = user_data["id"]

    playlist_data = sp.user_playlist_create(user_id, f"moodtape {mood}")
    playlist_id = playlist_data["id"]

    random.shuffle(tracks)
    sp.user_playlist_add_tracks(user_id, playlist_id, tracks[:30])

    return playlist_id
