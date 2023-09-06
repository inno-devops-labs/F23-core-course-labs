FROM python:3.11-alpine AS prepare

RUN adduser -D limiteduser && chown -R limiteduser /app

COPY . ./app

USER limiteduser
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

FROM prepare AS run

ENTRYPOINT ["python3", "app.py", "-prod"]