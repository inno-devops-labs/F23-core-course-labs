# Current Time in Moscow

A simple Python web app that displays the current time in Moscow.

- **Framework**: Flask
- **Testing**: unittest
- **Code style**: flake8 and black

## Docker

This application can be easily containerized using Docker. Below are instructions on how to build, pull, and run the Docker image.

1. Make sure you have Docker installed on your system.

2. Clone this repository to your local machine:

   ```
   git clone https://github.com/nikolina2k/core-course-labs.git
   ```

3. Navigate to the project directory:

   ```
   cd core-course-labs
   cd app_python
   ```

4. Build the Docker image manually:

   ```
   docker build -t nikolina2k/ma-repo .
   ```

5. Or pull the Docker Image from existing repo on Docker hub:

   ```
   docker pull nikolina2k/ma-repo:latest
   ```

6. Run the Docker Container:

   ```
   docker run -p 8000:8000 nikolina2k/ma-repo
   ```

The application will be accessible at http://localhost:8000 in your web browser.
