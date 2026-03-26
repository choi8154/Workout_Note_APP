from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import get_session_local


# 데이터베이스 세션을 생성하는 의존성 함수
def get_db() -> Generator[Session]:
    db = get_session_local()()  # 세션 생성
    try:
        yield db  # 세션을 반환 (yield는 제너레이터로, FastAPI가 자동으로 관리)
    finally:
        db.close()  # 요청이 끝나면 세션 닫기
