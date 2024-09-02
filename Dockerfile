FROM python:3.11.2-slim
LABEL authors="ducksu"

WORKDIR /app

# /app 디렉토리에 pyproject.toml, poetry.lock 파일을 복사
COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry install

COPY . /app/

EXPOSE 8000

# Buffered Off = 즉시 출력
ENV PYTHONUNBUFFERED=1

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]