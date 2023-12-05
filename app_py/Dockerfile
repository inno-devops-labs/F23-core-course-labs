FROM python:3.8-alpine
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
RUN adduser -D -g '' newuser
USER newuser
WORKDIR /home/newuser
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0", "app:app"]
