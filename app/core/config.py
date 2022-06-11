from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    """App Settings"""

    api_prefix: str = "/api/v1/cofee"
    app_mode: str = "Development"
    app_name: str = "making-coffee"
    cors_origins: List[AnyHttpUrl] = []
    database_url: str = "sqlite://:memory:"  # Default is a sqlite in memory
    database_models: list = ["schemas"]
    port: int = 8000
    secret_key: str = "SuperSecretKey"

    class Config:
        case_sensitive: bool = False


settings = Settings()
