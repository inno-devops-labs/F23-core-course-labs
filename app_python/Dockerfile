FROM python:3.11.5-slim

WORKDIR /app_python
COPY requirements/requirements-prod.txt requirements-prod.txt

RUN pip install -r requirements-prod.txt

COPY ./src ./src

RUN addgroup --system user && adduser --system --group user
USER user

EXPOSE 5000
ENTRYPOINT [ "python3", "src/app.py" ]
