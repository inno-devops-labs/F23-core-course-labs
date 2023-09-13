# Use an official Python runtime as a parent image
FROM python:3-alpine3.15

# Set the working directory in the container
WORKDIR /app 

# Copy all of the application files in the container
COPY . /app

# Create user and set ownership and permissions as required
# Install any needed packages specified in requirements.txt
RUN adduser myuser -D && chown -R myuser /app \
    && pip install --no-cache-dir -r requirements.txt 

# Pick the running user
USER myuser

# Expose the port of the Flask app
EXPOSE 8080

# Start the Flask app
CMD ["python", "./app.py"]
