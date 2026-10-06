# this is used so for strongly typed python objects
# we use this instead of writing os.environ.get stuff
# python checks these settings everytime after starting

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "MinBox"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"


    DATABASE_URL: str = (
        "postgresql+asyncpg://minbox_user:minbox_password@localhost:5432/minbox_dev"
    )


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Creating a single cached instance of settings to be imported across the app
settings = Settings()
