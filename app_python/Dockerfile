FROM python:3.10-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

RUN useradd --system --uid 1000 --group users appuser

USER appuser

RUN pytest tests

EXPOSE 5000

CMD ["python", "run.py"]
