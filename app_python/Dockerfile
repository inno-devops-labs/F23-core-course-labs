FROM python:3.10

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/__init__.py ./

RUN useradd -ms /bin/bash user_start && chown -R user_start /app/
USER user_start

ENV PYTHONPATH .
ENTRYPOINT ["python3", "main.py"]