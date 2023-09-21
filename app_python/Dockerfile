# use base image with specific versions
FROM python:3.10-slim

# Create a low privileged user
RUN useradd -m myuser

# Create and set the working directory
WORKDIR /app

# Copy requirements file mreqfdocker.txt
COPY mreqfdocker.txt .

# Install application dependencies (as myuser)
RUN pip install --no-cache-dir -r mreqfdocker.txt

# Copy the rest of the needed application files
COPY . /app

# Change ownership of the copied files to myuser
RUN chown -R myuser /app

# Switch to the new user
USER myuser

# Run your application (as myuser)
CMD ["python3", "app.py"]
