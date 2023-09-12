FROM python:3.11.4-slim-buster

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./main.py /code/

RUN chmod a-wx main.py && useradd -ms /bin/bash myuser
USER myuser

EXPOSE 8000
ENTRYPOINT ["python3", "-m", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]