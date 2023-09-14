# Use the official Python image as the base
FROM python:3.10.8

RUN useradd -m -d /home/xyz -s /bin/bash xyz

WORKDIR /app
EXPOSE 8000

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./templates /app/templates
COPY ./main.py /app/

USER xyz

CMD ["uvicorn", "main:app", "--host=127.0.0.1", "--port=8000"]