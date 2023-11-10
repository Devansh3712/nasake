run:
	gunicorn -c gunicorn.conf.py main:app

dev:
	uvicorn main:app --reload
