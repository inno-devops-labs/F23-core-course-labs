# Используем базовый образ Python
FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

RUN pip install django

COPY . /app/

RUN adduser -D rootlessuser $$ chown -R rootlessuser /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
