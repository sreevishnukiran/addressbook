from fastapi import FastAPI, Request
import time
import logging

from add_book.db import Base, engine
from add_book.routes.address import router as address_router
from add_book.logging_config import setup_logging

setup_logging()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

logger = logging.getLogger("app")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"Status: {response.status_code} "
        f"Time: {duration:.3f}s"
    )
    return response

app.include_router(address_router)