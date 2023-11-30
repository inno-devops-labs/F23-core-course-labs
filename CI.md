# CI best practices

Azamat Shakirov B20-CS

a.shakirov@innopolis.university



**Trigger on specific events:**

The `on: [push]` configuration ensures that the CI workflow is triggered only when there is a push event to the repository. This helps in avoiding unnecessary CI runs and improves performance.

**Specify the operating system for the runner:**

The `runs-on: ubuntu-latest` configuration specifies that the CI workflow should run on an Ubuntu operating system. It is important to specify the appropriate operating system to ensure compatibility and consistency in the build environment.

**Use versioned actions:**

The `actions/checkout@v2`, `actions/setup-python@v2`, `snyk/actions/python-3.9@master`, `docker/login-action@v3`, `docker/setup-buildx-action@v3`, and `docker/build-push-action@v5` actions are all using specific versions. This ensures that the workflow uses stable and tested versions of these actions, reducing the risk of unexpected behavior due to updates in the actions.

**Set up Python environment:**

The `actions/setup-python@v2` action is used to set up the Python environment with a specific version (`python-version: 3.9`) and caching (`cache: 'pip'`). This helps in ensuring that the Python dependencies are installed correctly and consistently.

**Install dependencies:**

The `pip install -r ./lab1/app_python/requirements.txt` step installs the project dependencies specified in the `requirements.txt` file. This ensures that the required dependencies are available for linting, testing, and building the project.

**Code linting:**

The `flake8` step runs the flake8 linter on the `./lab1/app_python/` directory to check for code style and formatting issues. Linting helps maintain code quality and consistency.

**Unit testing:**

The `pytest` step runs the unit tests located in the `./lab1/app_python/test.py` file. Running tests ensures that the code behaves as expected and helps catch any regressions or issues.

**Security vulnerability scanning:**

The `snyk/actions/python-3.9@master` action is used to run Snyk to check for vulnerabilities in the project. This step helps identify any security vulnerabilities in the dependencies and allows for proactive remediation.

**Docker image building and pushing:**

The `docker/login-action@v3`, `docker/setup-buildx-action@v3`, and `docker/build-push-action@v5` actions are used to build and push a Docker image based on the `./lab1/Dockerfile`. This allows for containerization of the application and easy deployment to a container registry.

**Use secrets for sensitive information:**

The sensitive information such as Docker credentials (`DOCKER_USERNAME` and `DOCKER_PASSWORD`) and Snyk token (`SNYK_TOKEN`) are stored as secrets and accessed using the `${{ secrets.SECRET_NAME }}` syntax. Storing sensitive information as secrets helps protect them from exposure in the CI workflow logs or repository.