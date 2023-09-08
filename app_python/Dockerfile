FROM python:3.11-alpine AS prepare

COPY . /app

RUN adduser -D limiteduser && chown -R limiteduser /app

USER limiteduser
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

FROM prepare AS runtime

EXPOSE 8000

ENTRYPOINT ["python3", "app.py", "-prod"]