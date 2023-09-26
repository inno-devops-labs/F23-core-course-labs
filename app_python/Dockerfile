# Use the official Python image as a base
FROM python:3.10-slim

# Create a non-root user and group
RUN groupadd -r usergroup && useradd -r -g usergroup nonrootuser

# Set the working directory
WORKDIR /app_python

# Update package index, install packages, and clean up in one step
RUN apt-get update -y && \
    apt-get install -y tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Change ownership of the application directory to the non-root user
RUN chown -R nonrootuser:usergroup /app_python

# Copy requirements file separately to optimize caching
COPY requirements.txt .

# Install required Python packages with caching disabled
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the necessary port
EXPOSE 5000

# Switch to the non-root user
USER nonrootuser

# Set environment variables for the Flask application
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Use CMD instead of ENTRYPOINT for flexibility
CMD ["flask", "run"]