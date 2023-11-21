FROM python:3.7

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd -u 1000 -m aboba

USER aboba

WORKDIR /code

COPY ./app_python /code/app_python

CMD ["uvicorn", "app_python.main:app", "--host", "0.0.0.0", "--port", "8000"]
