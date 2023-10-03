# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' myuser
USER myuser

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run web_app.py when the container launches
CMD ["python", "web_app.py"]
