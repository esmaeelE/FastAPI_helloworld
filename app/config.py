from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_")

    app_name: str = "My API"
    app_version: str = "1.0.0"
    app_env: str = "development"
    log_level: str = "INFO"


settings = Settings()
