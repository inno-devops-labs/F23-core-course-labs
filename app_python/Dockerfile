# Dockerfile, Image, Container
FROM python:3.9.6

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \ 
    && addgroup -S app && adduser -S app -G app \
    && chown -R app:app . 

COPY . .

EXPOSE 5000

USER app

CMD ["gunicorn", "--bind", "127.0.0.1:5000", "main.py"]