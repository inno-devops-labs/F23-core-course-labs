FROM python:3.9-slim-buster

RUN useradd -m --no-log-init pythonuser
USER pythonuser

WORKDIR /app

RUN python3 -m venv /app/env
ENV PATH="/app/env/bin:$PATH"

COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .


EXPOSE 5000

CMD ["python", "app.py"]