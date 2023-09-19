FROM python:3.10-alpine

COPY . /app

RUN adduser simpleuser -D && chown -R simpleuser /app

USER simpleuser

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]