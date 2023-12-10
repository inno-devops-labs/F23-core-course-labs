# Standard base python image
FROM python:3.9

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy all files of the application into container
COPY . /app/

# Copy the requirements file into the container
COPY requirements.txt /app/

# Upgrade pip and install dependencies without caching
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# To enhance security, add a non-root user
RUN useradd --create-home myuser && chown -R myuser /app

# Switch to new user
USER myuser

# Set the port
EXPOSE 8080

# Run the app
CMD [ "python", "app.py" ]