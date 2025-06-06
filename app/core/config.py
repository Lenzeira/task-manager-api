from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "sua-chave-secreta-aqui"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./database.db"

    class Config:
        env_file = ".env"

settings = Settings()
