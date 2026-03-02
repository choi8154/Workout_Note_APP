from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_SCHEME: str
    DB_PORT: str
    DB_HOST: str

    @property
    def DATABASE_URL(self):
        return f"{self.DB_SCHEME}+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
