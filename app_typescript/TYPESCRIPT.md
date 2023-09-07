# A web app that shows you cat pictures

## Framework

This web app was built using React.js library to create a UI that generates pictures of cats for people who want to see them and people who don't.

## Applied best practices

- **Project Structure**: Followed a well-structured project layout.
- **Version Control**: Used Git to track changes in the codebase.
- **Testing**: The app was manually tested to validate the app's functionality.
- **Pre-commit hooks**: Pre-commit hooks were implemented to automate code formatting and enforce coding standards. Prettier and linters were integrated into the development workflow to ensure consistent code quality before each commit.
- **Git submodule**: Git submodules were employed to manage external dependencies effectively.

## Docker

This application can be easily containerized using Docker. Below are instructions on how to build, pull, and run the Docker image.

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository to your local machine:

   ```
   git clone https://github.com/nikolina2k/core-course-labs.git
   ```

3. Navigate to the project directory:

   ```
   cd core-course-labs
   cd app_typescript
   cd cat-pics
   ```

4. Build and run the Docker image using Docker Compose:

   ```
   docker-compose up -d --build
   ```

5. Or pull the Docker Image from existing repo on Docker hub:

   ```
   docker pull nikolina2k/cat-pics
   ```

6. Run the Docker Container:

   ```
   docker run -p 3001:80 nikolina2k/cat-pics
   ```

The application will be accessible at http://localhost:3001 in your web browser.
