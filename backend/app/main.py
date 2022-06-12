from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.db import init_database
from app.api import router
from app.core.config import settings


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

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)
