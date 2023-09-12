# Use an official Python runtime as a parent image
FROM python:3.10-slim-bullseye

# Create and set the working directory in the container
WORKDIR /app

ARG port=1010

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=$port

# Copy the application code into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE $port

# Add new non-root user
RUN useradd defaultuser

# Use this user to make container root-less
USER defaultuser

# Define the command to run your application
CMD ["flask", "run"]
