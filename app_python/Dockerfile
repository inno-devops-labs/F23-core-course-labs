FROM python:3.10.12


WORKDIR /app
COPY main.py /app/
COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8008
CMD ["python", "main.py"]
