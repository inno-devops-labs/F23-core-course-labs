FROM python:3-alpine

COPY . ./msk_time

RUN adduser newuser -D && chown -R newuser /msk_time

USER newuser
WORKDIR /msk_time

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
