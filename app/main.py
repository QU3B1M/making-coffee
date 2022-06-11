from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db import init_database
from api import router
from core.config import settings


app = FastAPI()

init_database(app=app)

# Set all CORS enabled origins
if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router)
