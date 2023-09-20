# Используем базовый образ Python
FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN useradd -m --no-log-init appuser
USER appuser

RUN mkdir /app

WORKDIR /app

COPY app_python/requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
