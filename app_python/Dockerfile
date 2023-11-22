FROM python:3.10-alpine

WORKDIR /app

RUN adduser -D user1 && chown -R user1 /app && mkdir volume

RUN touch volume/visits.txt

COPY . .

EXPOSE 8080

RUN pip install  -r requirements.txt

USER user1

CMD ["python", "index.py"]