FROM python:3.7

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN adduser -D -g '' aboba

USER aboba

WORKDIR /code

COPY ./app_python /code/app_python

CMD ["uvicorn", "src.app:app", "--host", "localhost", "--port", "8000"]
