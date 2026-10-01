from functools import lru_cache
from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Library Catalog API"
    environment: Literal["development", "staging", "production"] = "development" 
    debug: bool = False
    database_url: PostgresDsn
    database_pool_size: int = 20
    api_v1_prefix: str = "/api/v1"
    log_level: str = "INFO"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openlibrary_base_url: str = "https://openlibrary.org"
    openlibrary_timeout: float = 10.0
    openlibrary_max_connections: int = 20
    openlibrary_max_keepalive: int = 10
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )
    
    @property
    def is_production(self) -> bool:
        return self.environment == "production"
    
    @property
    def cors_origins(self) -> list[str]:
        """CORS origins зависят от environment."""
        if self.environment == "development":
            return ["*"]
        return ["http://localhost:3000"]
    
    @property
    def cors_allow_credentials(self) -> bool:
        """Credentials только если не wildcard."""
        return self.environment != "development"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
