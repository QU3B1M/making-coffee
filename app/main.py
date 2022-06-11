# Third-party imports
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db import init_database
from api import router
from core.config import settings


app = FastAPI()

init_database(app=app)

# Set all CORS enabled origins
if settings.cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router)
