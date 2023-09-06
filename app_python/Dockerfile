# pull official base image
FROM python:3.10

# Create a non-root user named 'cooluser'
RUN useradd -m cooluser

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /app

# Create and set the working directory
WORKDIR /app

# Copy the Django project code into the container
COPY . /app/


# Install any dependencies (You may need to adjust this based on your project setup)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Switch to the 'django' user
USER cooluser

# Specify the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
