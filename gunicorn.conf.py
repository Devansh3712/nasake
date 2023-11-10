from multiprocessing import cpu_count

from config import settings

bind = f"{settings.HOST}:{settings.PORT}"
workers = 2 * cpu_count() + 1
worker_class = "uvicorn.workers.UvicornWorker"
