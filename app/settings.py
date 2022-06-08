import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """App Settings"""

    database_url: str = "sqlite://:memory:"  # Default is a sqlite in memory
    database_models: list = ["api.database.schemas"]
    app_mode: str = "Development"
    app_name: str = "making-coffee"
    api_prefix: str = "/api/v1/cofee"
    secret_key: str = "SuperSecretKey"
    algorithm: str = "HS256"
    port: int = 8000

    class Config:
        case_sensitive: bool = True
        env_file = os.path.expanduser(".env")