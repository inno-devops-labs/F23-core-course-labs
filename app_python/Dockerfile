FROM python:3.11.5-alpine

WORKDIR /app

COPY . /app

RUN adduser myuser -D && chown -R myuser /app \
    && pip3 install -r requirements.txt

USER myuser

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python3", "app.py"]