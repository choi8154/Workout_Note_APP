from fastapi import FastAPI

app = FastAPI()

# @app.on_event("startup") # FastAPI 이벤트 시스템으로 앱 시작 시 실행할 함수를 정의할 수 있음.
# def startup_event():
#     # 여기에 데이터베이스 연결이나 초기화 작업 수행 가능.
#     def on_startup():
#         Base.metadata.create_all(bind=engine)  # 데이터베이스 테이블 생성


@app.get("/")
# 테스트 ORM 모델. 실제 프로젝트에서는 삭제.
def test_route() -> dict[str, str]:
    return {"message": "Hello, World!"}
