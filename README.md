# nasake
*Nasake* is a japanese word that means sympathy and affection. It is a web app for different mental health resources at one place.

## Installation
- Clone the repository
- Create a python virtual environment
```shell
python3 -m venv venv
```
- Install dependencies via `poetry` or `requirements.txt`
```shell
# poetry
pip install poetry
poetry install

# requirements.txt
pip install -r requirements.txt
```
- Copy contents of `.env.dev` to `.env` and add the environment variables
```shell
cp .env.dev .env
```
- Run the application
```shell
gunicorn -c gunicorn.conf.py server.app:app

# or using make
make run
```

## To-Do
- [ ] Dockerize application
- [ ] Create login for therapists
- [ ] Add movie/song recommendations based on journal entry
- [ ] Work on the UI and UX
- [ ] Add meditation guides, zen mode
- [ ] Add crisis mode to chatbot (assistance in case of emergencies)