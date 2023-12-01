PY = venv/bin/python3

run:
	$(PY) -m gunicorn -c gunicorn.conf.py server.app:app

dev:
	$(PY) -m uvicorn server.app:app --reload

reqs:
	$(PY) -m poetry export -f requirements.txt --output requirements.txt --without-hashes
