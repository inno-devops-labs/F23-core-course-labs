FROM python:3

RUN pip install --no-cache-dir  \
    Flask  \
    pytz

WORKDIR /app
COPY ./main.py ./

RUN useradd -ms /bin/bash user_start && chown -R user_start /app/
USER user_start

ENV PYTHONPATH .
ENTRYPOINT ["python3", "main.py"]