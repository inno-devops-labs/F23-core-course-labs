# Start with a slim and official Python base image.
FROM python:3.11-slim

# Flask default port
EXPOSE 5000

# Set environment variables.
# Disabling bytecode for a cleaner container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensuring unbuffered mode for realtime logs.
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Upgrade pip and install dependencies, then clean up cache to minimize layers and reduce size.
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache

# Create a non-root user and switch to it.
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

# Copy the rest of the application code into the container.
COPY . .

# Healthcheck instruction to check the /health endpoint.
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1

# Command to run the application.
CMD [ "python", "app.py" ]
