# 프로젝트 초기 세팅

## 가상환경 잡기
- `pip install uv`: uv설치
- `uv sync`: 의존성 설치

<details>
<summary>사용법</summary>

- `uv add <패키지>`:
- ``:
- ``:
- ``:
- ``:
- ``:
</details>

## 환경변수 세팅
- envs 폴더 하위에 env.dev 파일 작성
```env
# envs/env.dev
DATABASE=mysql+pymysql
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=user
DATABASE_PASSWORD=pw123!
DATABASE_NAME=mydb
```

## 도커 빌드 및 실행
> 마이그레이션을 위해서 로컬에서 db를 열거나 귀찮으면 도커로 실행해야함.
- `docker compose -f docker/docker-compose.dev.yml up --build -d db`: db만 빌드하고 실행
- `docker compose -f docker/docker-compose.dev.yml down db`: 마이그레이션 했으면 필요에 따라 db 끄기

## 마이그레이션
- `alembic upgrade head`: 마이그레이션 적용

<details>
<summary>사용법</summary>

테이블 생성 후 아래 명령어를 치면 됨.
되도록이면 develop에서 rebase한 후 `alembic upgrade head`를 하고 작업할 것
- `alembic revision --autogenerate -m "생성/수정한 테이블 내용"`: 마이그레이션 파일 생성
- `alembic upgrade head`: 마이그레이션 적용
- `alembic downgrade -1`: 롤백 (다운그레이드)
- `alembic current`: 현재 상태 확인
- `alembic history`: 히스토리 보기
</details>

## 커밋 템플릿 적용
- `git config commit.template .gitmessage.txt`: 파일 적용
- 사용법은 `.gitmessage.txt`에서 확인

-------------------

## 5. 코드 최적화 툴 사용법
1. ruff

2. mypy

3. pytest

4. coverage

5. 

## 6. cd 구조

## 사용한 의존성
- cryptography
- slembic
- pymysql
- sqlalchemy

### 1) dev
- pytest-asyncio
- httpx
- asgi-lifespan
- respx

## etc.
1. 구글 워크 스페이스 cli


### 내일 할 것
토믈파일 수정 & ci/cd 구축 & 이슈템플릿 만들기 & 