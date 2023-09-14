FROM python:3.10.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./templates /app/templates
COPY ./main.py /app/

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8080"]