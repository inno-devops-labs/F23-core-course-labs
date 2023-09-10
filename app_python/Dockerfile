FROM python:3.10-slim AS base

WORKDIR /app

RUN useradd -ms /bin/bash appuser

COPY requirements.txt .

RUN pip install -r requirements.txt 

FROM base as test

COPY . .

RUN chown -R appuser:appuser /app

USER appuser

RUN pytest tests

FROM base as release

COPY --from=test --chown=appuser:appuser /app /app

USER appuser

EXPOSE 5000

CMD ["python", "run.py"]
