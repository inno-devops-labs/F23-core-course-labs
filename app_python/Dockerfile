FROM python:3.10
RUN useradd -m myuser && \
    mkdir /app && \
    chown myuser:myuser /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
USER myuser
CMD ["python", "app.py"]
