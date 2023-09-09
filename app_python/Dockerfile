FROM python:3.9.6-alpine

WORKDIR /app

RUN addgroup -g 2000 node && adduser -u 2000 -G node -s /bin/sh -D node

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY main.py /app/
EXPOSE 8000

USER node

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8000"]