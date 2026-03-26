from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings


# SQLAlchemy 설정
def get_engine() -> Engine:
    settings = get_settings()
    return create_engine(settings.DATABASE_URL, echo=True)  # echo=True는 SQL 쿼리를 로그로 출력.


def get_session_local() -> sessionmaker[Session]:
    return sessionmaker(autocommit=False, autoflush=False, bind=get_engine())  # 세션 클래스 생성
