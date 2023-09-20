# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

COPY ./setup/requirements.txt setup/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r ./setup/requirements.txt

# Copy the current directory contents into the container at /app
COPY ./scripts /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Create user and set ownership and permissions as required
RUN adduser --disabled-login myuser && chown -R myuser /app

# Set user for execution
USER myuser

# Command to run the application
CMD ["python", "app.py"]