# Use the official Python image as base
FROM python:3.10-slim

# Set the working directory
WORKDIR /app_python

# Update the package index and install required packages
RUN apt-get update -y && \
    apt-get install -y tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# We'll run the app on port 5000
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the command to start the application
CMD ["flask", "run"]