FROM python:3.11.5-alpine3.18

LABEL version="1.0" maintainer="Mikhail Dmitriev <m.dmitriev@innopolis.university>"

WORKDIR /python_app

RUN adduser -D newuser && chown -R newuser /python_app
USER newuser

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/ .

CMD [ "python3", "-m" , "flask", "--app", "index", "run", "-h", "0.0.0.0", "-p", "5555"]
