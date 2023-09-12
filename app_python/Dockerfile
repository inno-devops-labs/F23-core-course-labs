# Use official base image
FROM python:3.9-slim

# Set working directory for container
WORKDIR /app

# Copy file with project requirements
COPY requirements.txt .

# Upgrade pip and install python dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

# Make directory to start app as module
RUN mkdir "app_python"

# Copy all necessary files
COPY . ./app_python

# Create non-root user
RUN useradd -m user

# Run app as non-root user
USER user

# Expose ports
EXPOSE 8080 8080

# Run app
ENTRYPOINT ["python3", "-m", "app_python"]