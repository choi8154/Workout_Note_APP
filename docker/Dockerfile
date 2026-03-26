FROM python:3.14-slim

# 빌드/런타임에 필요한 시스템 패키지
RUN apt-get update && apt-get install -y --no-install-recommends \
	curl \
	&& rm -rf /var/lib/apt/list/*

# 도커상의 작업 디렉토리 설정
WORKDIR /app

# uv 설치
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir uv

# 의존성 기록파일 복사
COPY pyproject.toml uv.lock ./

# 의존성 설치 (개발 의존성 제외)
RUN uv sync --locked --no-dev --no-install-project

# 애플리케이션 소스 코드 복사
COPY . .

# 컨테이너가 수신 대기할 포트 노출
EXPOSE 8000

# 애플리케이션 실행 명령
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
