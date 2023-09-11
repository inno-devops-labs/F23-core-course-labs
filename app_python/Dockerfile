# Use a specific Python version
FROM python:3.10

# Create a non-root user named 'cooluser'
RUN useradd -m cooluser

# Create and set the working directory
WORKDIR /app

# Copy just the requirements file to leverage Docker cache
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . /app/

# Change ownership of the copied files and directories to 'cooluser'
RUN chown -R cooluser /app

# Switch to the 'cooluser' user
USER cooluser

# Specify the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
