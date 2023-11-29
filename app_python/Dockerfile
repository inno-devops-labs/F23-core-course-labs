FROM python:3.9-slim

RUN useradd -m -d /home/xyz -s /bin/bash xyz
RUN mkdir -p /app/data && echo "0" > /app/data/global_counter.txt

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R xyz:xyz /app

# Set permissions for the data directory
RUN chmod -R 755 /app/data

USER xyz

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]