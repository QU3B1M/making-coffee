from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    '''App Settings'''

    API_PREFIX: str = '/api/v1/cofee'
    APP_MODE: str = 'Development'
    APP_NAME: str = 'making-coffee'
    CORS_ORIGINS: List[AnyHttpUrl] = []
    DATABASE_URL: str = 'sqlite://:memory:'  # Default is a sqlite in memory
    DATABASE_MODELS: list = ['app.schemas']
    PORT: int = 8000
    SECRET_KEY: str = 'SuperSecretKey'

    class Config:
        case_sensitive: bool = True


settings = Settings()
