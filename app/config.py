from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My API"
    app_version: str = "1.0.0"
    app_env: str = "development"
    log_level: str = "INFO"

    model_config = {"env_prefix": "APP_"}


settings = Settings()
