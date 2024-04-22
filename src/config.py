from pydantic_settings import BaseSettings
from pydantic import Field


class EnvSetting(BaseSettings):

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'
        extra = 'allow'


class MongoSettings(EnvSetting):
    database: str = Field(alias='MONGO_INITDB_DATABASE')
    collection: str = Field(alias='MONGO_INITDB_COLLECTION')
    username: str = Field(alias='MONGO_INITDB_ROOT_USERNAME')
    password: str = Field(alias='MONGO_INITDB_ROOT_PASSWORD')
    host: str = Field(alias='MONGO_INITDB_HOST')
    port: str = Field(alias='MONGO_INITDB_PORT')


class BotSettings(EnvSetting):
    token: str = Field(alias='BOT_TOKEN')


class Settings(BaseSettings):
    mongo: MongoSettings = MongoSettings()
    bot: BotSettings = BotSettings()
    mongo_uri: str = f"mongodb://{mongo.username}:{mongo.password}@{mongo.host}:{mongo.port}/{mongo.database}?authSource=admin"


settings = Settings()
