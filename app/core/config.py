from typing import Optional

from pydantic import EmailStr, BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Product Markup'
    app_description: str = 'Приложение для автоматизации процесса сопоставления товаров'
    database_url: str = 'sqlite+aiosqlite:///./prosept.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    first_superuser_name: Optional[str] = None
    first_superuser_last_name: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
