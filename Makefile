PY = venv/bin/python3

run:
	$(PY) -m gunicorn -c gunicorn.conf.py server.api:app

dev:
	$(PY) -m uvicorn server.api:app --reload

reqs:
	$(PY) -m poetry export -f requirements.txt --output requirements.txt --without-hashes
