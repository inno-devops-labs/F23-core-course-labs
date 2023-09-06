FROM python:3.11.5-alpine3.17 AS release

RUN adduser www-data --system --shell=/bin/false
USER www-data

WORKDIR /app_python
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 
WORKDIR /

ENV HOST="0.0.0.0"
ENV PORT="8000"

CMD ["sh", "-c", "python3 -m gunicorn --bind $HOST:$PORT app_python.wsgi:app"]