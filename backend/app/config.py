# app/config.py
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str = "postgresql://postgres:password@localhost/netflix_db"
#     JWT_SECRET_KEY: str = "26f6c97c6a1df014993afbee006d1c71"
#     JWT_ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

#     class Config:
#         env_file = ".env"

# settings = Settings()


from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # ✅ ensures .env is read

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()


