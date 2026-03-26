from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # DB 설정
    DATABASE: str
    DATABASE_HOST: str
    DATABASE_PORT: int = 3306
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str

    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DATABASE}://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

    # 기타 설정 추가 가능
    model_config = SettingsConfigDict(
        env_file="envs/.env.dev",  # 환경 변수 파일 경로 설정
        env_file_encoding="utf-8",  # 환경 변수 파일 인코딩 설정
        case_sensitive=True,  # 환경 변수 이름 대소문자 구분 여부 설정
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
