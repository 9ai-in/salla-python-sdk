from pydantic import BaseSettings
from typing import Union


class Settings(BaseSettings):
    """
    All necessary Environment Variables
    """

    CLIENT_ID: Union[str, None]
    CLIENT_SECRET: Union[str, None]
    ACCESS_TOKEN: Union[str, None]
    REFRESH_TOKEN: Union[str, None]
    WEBHOOK_SECRET: Union[str, None]

    class Config:
        env_file = ".env"


ENV = Settings()
