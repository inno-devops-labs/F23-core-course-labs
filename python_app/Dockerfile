FROM python:3.9-slim

# Set the working directory to /python_app
WORKDIR /python_app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Upgrade the pip and install the required Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the main content of the project to the working directory
COPY . /python_app

# Create a non-root user to run the application
RUN groupadd -r limiteduser && useradd -r -g limiteduser limiteduser

# Set the ownership and permissions for the working directory
RUN chown -R limiteduser:limiteduser /python_app
RUN chmod -R 755 /python_app

# Switch to the non-root user
USER limiteduser

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the container port
EXPOSE 5000

# Run the application
CMD ["flask", "run"]