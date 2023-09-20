FROM python:3.9

RUN useradd -m --no-log-init appuser
USER appuser

WORKDIR /app

RUN pip install django

COPY . /app/

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]