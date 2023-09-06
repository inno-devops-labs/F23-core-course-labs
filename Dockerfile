FROM python:3.10.8

WORKDIR /app

EXPOSE 8000

COPY ./app_python/requirements.txt  /app/requirements.txt

RUN pip install -r ./app_python/requirements.txt

COPY ./app_python/templates /app/templates
COPY ./app_python/main.py /app/

CMD [ "uvicorn", "main:app", "--host=127.0.0.1", "--port=8000" ]