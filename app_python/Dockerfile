FROM python:3.10

WORKDIR /app
EXPOSE 5000

RUN useradd --create-home user && chown -R user:user /app
USER user

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 

CMD ["python3", "app.py"]