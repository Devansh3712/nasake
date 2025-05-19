import random
import requests
from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Dictionary to store user watchlists (replace global 'watchlist')
user_watchlists = {}

# Add user session management (for simplicity, we use a session cookie)
def get_or_create_session(session_token: str = Cookie(None)):
    if session_token not in user_watchlists:
        user_watchlists[session_token] = {"watchlist": [], "movies_list": []}
    return user_watchlists[session_token]

templates = Jinja2Templates(directory="templates")

# List of movies
initial_movies_list = [
    "The Shawshank Redemption",
    "Forrest Gump",
    "Good Will Hunting",
    "It's a Wonderful Life",
    "Dead Poets Society",
    "Amélie",
    "The Pursuit of Happyness",
    "Groundhog Day",
    "The Intouchables",
    "Inside Out",
    "The Blind Side",
    "Silver Linings Playbook",
    "Good Morning, Vietnam",
    "Eternal Sunshine of the Spotless Mind",
    "The King's Speech",
    "Life is Beautiful",
    "A Beautiful Mind",
    "The Bucket List",
    "The Help",
    "Patch Adams",
    "Big Fish",
    "Eat Pray Love",
    "Into the Wild",
    "The Perks of Being a Wallflower",
    "The Secret Life of Walter Mitty",
    "October Sky",
    "The Theory of Everything",
    "Little Miss Sunshine",
    "The Truman Show",
    "Up",
    "Toy Story series",
    "Finding Nemo",
    "The Lion King",
    "The Sound of Music",
    "Mary Poppins",
    "The Karate Kid",
    "Rocky",
    "The Grand Budapest Hotel",
    "Stand and Deliver",
    "The Green Mile",
    "Soul",
    "Kramer vs. Kramer",
    "Goodbye Lenin!",
    "Ratatouille",
    "Billy Elliot",
    "The Breakfast Club",
    "A Street Cat Named Bob",
    "The Greatest Showman",
    "The Fault in Our Stars",
    "A Beautiful Day in the Neighborhood",
    "Good Morning, Sunshine",
    "The Social Network",
    "The Art of Racing in the Rain",
    "The Wizard of Oz",
    "Whale Rider",
    "Perks of Being a Wallflower",
    "Little Miss Sunshine",
    "Legally Blonde",
    "The Bridges of Madison County",
    "The Pursuit of Happyness",
    "Spirited Away",
    "Coco",
    "The Theory of Everything",
    "The Help",
    "The Green Book",
    "Room",
    "Thanks for Sharing",
    "It’s Kind of a Funny Story",
    "The Fisher King",
    "Ordinary People",
    "Ma Vie en Rose",
    "Antwone Fisher",
    "The Prince of Tides",
    "One Flew Over the Cuckoo's Nest",
    "It’s Complicated",
    "Couples Retreat",
    "A Beautiful Mind",
    "Silver Linings Playbook",
    "The Soloist",
    "Good Will Hunting",
    "A Beautiful Boy",
    "A Star is Born",
    "500 Days of Summer",
    "The Basketball Diaries",
    "Trainspotting",
    "Being Charlie",
    "The Anonymous People",
    "The Story of the Weeping Camel",
    "Still Alice",
    "The King of Staten Island",
    "Leaving Las Vegas",
    "Little Miss Sunshine",
    "The Skeleton Twins",
    "It’s Kind of a Funny Story",
    "The Perks of Being a Wallflower",
    "The Incredibles",
    "Shrek",
    "Despicable Me",
    "Frozen",
    "Finding Dory",
    "Toy Story",
    "Zootopia"
]

def get_movie_info(title):
    # Make a request to OMDB API
    API_KEY = '4807f5fc'  # Replace with your actual API key
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    response = requests.get(url)
    data = response.json()
    imdb_id = data.get('imdbID')
    return imdb_id, data

@app.get('/', response_class=HTMLResponse)
def index(request: Request, session_token: str = Cookie(None)):
    # Get or create session and initialize movies list if needed
    session_data = get_or_create_session(session_token)
    if not session_data["movies_list"]:
        session_data["movies_list"] = initial_movies_list.copy()

    # Choose a random movie title from session's movies_list
    random_title = random.choice(session_data["movies_list"])
    session_data["movies_list"].remove(random_title)  # Remove selected movie from the list
    
    # Get movie information from OMDB API
    imdb_id, movie_info = get_movie_info(random_title)
    
    return templates.TemplateResponse("index.html", {"request": request, "movie_info": movie_info})

@app.post('/add_to_watchlist')
async def add_to_watchlist(title: str = Form(...), session_token: str = Cookie(None)):
    watchlist = get_or_create_session(session_token)["watchlist"]
    watchlist.append(title)
    # Return success message (handled by JavaScript)
    return "Added to Watchlist"

@app.get('/watchlist', response_class=HTMLResponse)
def show_watchlist(request: Request, session_token: str = Cookie(None)):
    watchlist = get_or_create_session(session_token)["watchlist"]
    return templates.TemplateResponse("watchlist.html", {"request": request, "watchlist": watchlist})

# Add route to remove movies from watchlist
@app.get('/remove_from_watchlist')
async def remove_from_watchlist(title: str, session_token: str = Cookie(None)):
    watchlist = get_or_create_session(session_token)["watchlist"]
    if title in watchlist:
        watchlist.remove(title)
        return f"Removed '{title}' from watchlist!"
    else:
        return f"'{title}' not found in watchlist!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
