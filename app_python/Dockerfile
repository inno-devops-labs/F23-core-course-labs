FROM python:3.11.5-alpine3.17 AS release

RUN adduser www-data --system --shell=/bin/false

WORKDIR /app_python
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 
WORKDIR /

RUN chown -R www-data:www-data /app_python/data
USER www-data

ENV HOST="0.0.0.0"
ENV PORT="8000"
ENV APP_DIR="/app_python"
EXPOSE $PORT


CMD ["sh", "-c", "python3 -m gunicorn --bind $HOST:$PORT app_python.wsgi:app"]