from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings


def init_database(app: FastAPI):
    """Initializes the database connection"""
    register_tortoise(
        app,
        db_url=settings.DATABASE_URL,
        modules={
            "models": settings.DATABASE_MODELS,
        },
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(models_paths=settings.DATABASE_MODELS, app_label="models")
