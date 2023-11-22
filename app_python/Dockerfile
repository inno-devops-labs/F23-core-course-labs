FROM python:3.10-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

RUN useradd --system --uid 1000 --group users appuser

RUN chown -R appuser:users /app

USER appuser

ENV VISITSFILE=/app/visits

RUN if [ ! -f "$VISITSFILE" ]; then touch "$VISITSFILE"; fi

RUN pytest tests

EXPOSE 5000

CMD ["python", "run.py"]
