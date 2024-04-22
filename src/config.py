from pydantic_settings import BaseSettings
from pydantic import Field


class MongoSettings(BaseSettings):
    uri: str = Field(alias='DATABASE_URI')
    database: str = Field(alias='MONGO_INITDB_DATABASE')
    collection: str = Field(alias='MONGO_INITDB_COLLECTION')

    class Config:
        env_file = "../.env"
        env_file_encoding = 'utf-8'
        extra = 'allow'


class Settings(BaseSettings):
    mongo: MongoSettings = MongoSettings()


settings = Settings()
