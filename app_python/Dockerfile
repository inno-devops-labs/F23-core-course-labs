FROM python:3.9-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
VOLUME ["./volume/visits.txt", "./volume/visits.txt"]
RUN adduser -D myuser && chown -R myuser /app
RUN touch volume/visits.txt
RUN pip install -r requirements.txt
COPY . /app
USER myuser
ENV APP_TMP_DATA=/tmp
ENTRYPOINT ["/app"]
ENTRYPOINT ["python"]
CMD ["main.py"]