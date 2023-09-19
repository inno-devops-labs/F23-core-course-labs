RUN adduser -D -u 1001 myuser

USER myuser

FROM python:3.11-alpine

WORKDIR /app_python

COPY . /app_python

# Install needed packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 755 /app

EXPOSE 8000

CMD ["python", "-m", "venv", ".venv", "&&", ".venv/Scripts/Activate", "&&", "flask", "run"]
#CMD ["python -m venv .venv && . .venv/bin/activate.bat && flask run"]
