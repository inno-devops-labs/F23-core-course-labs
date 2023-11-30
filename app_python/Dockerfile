# Official Python runtime as the base image
FROM python:3.9-slim

# Creating a new user
RUN useradd -ms /bin/bash pythonuser \
    && chown -R pythonuser:pythonuser /home/pythonuser

# Working directory in the container
WORKDIR /home/pythonuser/app

# Copy the requirements file
COPY requirements.txt .

# Install the required Python packages and clean up
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY main.py .

# Folder for assets
RUN mkdir /assets && chown pythonuser /assets
VOLUME ["/assets"]

# Switch to the new user
USER pythonuser

# Specifing the command to run the application as the new user
CMD ["python3", "main.py"]