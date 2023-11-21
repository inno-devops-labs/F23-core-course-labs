FROM python:3.11

RUN useradd --create-home user
USER user

WORKDIR /code

COPY --chown=user:user ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY --chown=user:user ./main.py /code/

COPY --chown=user:user ./storage/visits /code/storage/visits

EXPOSE 80/tcp

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
