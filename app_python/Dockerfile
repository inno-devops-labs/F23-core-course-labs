FROM python:3.8-slim-buster

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py /app/main.py

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]