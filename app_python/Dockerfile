FROM python:3-slim

COPY . /app_python

RUN pip install --no-cache-dir -r /app_python/requirements.txt

WORKDIR /app_python/src

EXPOSE 8000/tcp

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
