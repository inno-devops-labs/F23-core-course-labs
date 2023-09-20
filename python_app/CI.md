## CI practices used in the code:

- **Separation of workflows**: The code includes separate workflows for "checks" and "build-deploy" which helps to organize and isolate different stages of the CI process.

- **Event-based triggering**: The workflow is triggered on push events with specific paths, ensuring that it only runs when relevant code changes are made.

- **Version management**: The "checks" job uses a matrix strategy to specify the Python version, allowing for testing across multiple versions simultaneously.

- **Caching dependencies**: The "Cache the libs" step utilizes the actions/cache action to cache Python dependencies, improving workflow execution time by avoiding unnecessary installations.

- **Linter integration**: The "Lint the code" step runs pylint to perform code linting and enforce coding standards.

- **Testing integration**: The "Run unit tests" step executes the Python unit tests using unittest module, ensuring the correctness of the code.

- **Dependency vulnerability scanning**: The "Snyk test" step integrates with Snyk to scan for and identify any known vulnerabilities in the project's dependencies.

- **Dependency management**: The "Install required libs" step uses pip to install the project's required dependencies specified in the requirements.txt file.

- **Docker integration**: The "build-deploy" job includes steps to log in to DockerHub and build/push a Docker image, enabling containerization and deployment of the application.

- **Secrets management**: The code references sensitive information (e.g., DockerHub credentials and Snyk token) using GitHub secrets, ensuring secure access to this information.