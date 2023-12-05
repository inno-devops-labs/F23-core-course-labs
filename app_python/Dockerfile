FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D newuser && chown -R newuser /app

USER newuser

EXPOSE 80

ENTRYPOINT ["python3", "app.py", "-prod"]