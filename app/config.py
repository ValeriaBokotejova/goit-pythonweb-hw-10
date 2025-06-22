from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str

    # JWT config
    secret_key: str
    algorithm: str = "HS256"
    token_expire_minutes: int = 30

    # Cloudinary
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    # Email config
    mail_username: EmailStr
    mail_password: str
    mail_server: str = "smtp.gmail.com"
    mail_port: int = 587

    # Frontend
    frontend_base_url: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


settings = Settings()
