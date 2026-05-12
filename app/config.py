from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):

    model_config = ConfigDict(
        env_file='.env',
        env_file_encoding="utf-8",
        extra="ignore"
    )

    APP_NAME: str = 'URL Shortener'
    APP_VERSION: str = '0.0.1'
    DEBUG: bool = False
    
    #Настройка БД
    DATABASE_URL: str = 'sqlite:///./url_shortener.db'

settings = Settings()