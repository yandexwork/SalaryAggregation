from pydantic_settings import BaseSettings
from pydantic import Field


class EnvSetting(BaseSettings):

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'
        extra = 'allow'
class BotSettings(EnvSetting):
    token: str = Field(alias='BOT_TOKEN')


class Settings(BaseSettings):
    mongo: MongoSettings = MongoSettings()
    bot: BotSettings = BotSettings()


settings = Settings()
