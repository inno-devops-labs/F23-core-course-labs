FROM python:3.10

RUN mkdir -p /app

WORKDIR /app

RUN useradd -ms /bin/bash user1 && chown user1:user1 /app

COPY . .

EXPOSE 8080

RUN pip install  -r requirements.txt

USER user1

CMD ["python", "index.py"]