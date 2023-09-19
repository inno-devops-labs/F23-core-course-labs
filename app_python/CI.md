# Best Practices in Python CI Workflow

The "Python CI" workflow adheres to several best practices for continuous integration (CI) and automation. Below is an overview of the best practices applied in this workflow:

## Trigger on Specific Events

The workflow is triggered on the `push` event, but it is further refined by specifying paths that trigger the workflow. This ensures that the workflow only runs when changes are made to the `app_python/` directory or the workflow file itself, optimizing CI resource usage.

```yaml
on:
  push:
    paths:
      - "app_python/**"
      - ".github/workflows/python.yml"
```

## Caching Dependencies

Caching is implemented for Python dependencies and Docker layers. This caching mechanism improves build performance by reusing previously cached dependencies and layers when the same workflow runs again. It helps reduce the time required for the workflow to complete.

```yaml
- name: Cache&restore Python dependencies
  uses: actions/cache@v2
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

```yaml
- name: Cache Docker layers
  uses: actions/cache@v2
  with:
    path: ~/.docker
    key: ${{ runner.os }}-docker-${{ hashFiles('app_python/Dockerfile') }}
    restore-keys: |
      ${{ runner.os }}-docker-
```

## Version Control Integration

The workflow uses the `actions/checkout` action to fetch the latest code from the repository. This ensures that the workflow operates on the most up-to-date codebase.

```yaml
- name: Checkout code
  uses: actions/checkout@v4
```

## Automated Testing and Linting

The workflow includes steps for linting and running tests, promoting code quality and correctness. It uses Flake8 for linting and pytest for running tests. Any failures in these steps will prevent the workflow from proceeding further, ensuring code quality.

```yaml
- name: Lint
  run: flake8 . --per-file-ignores="test/conftest.py:E402"

- name: Run Tests
  run: pytest
```

## Security Scanning

The workflow integrates security scanning by installing the Snyk CLI and using it to test for vulnerabilities in all projects. Secrets are appropriately managed for security, with the `SNYK_TOKEN` being stored in GitHub secrets.

```yaml
- name: Install Snyk CLI
  run: npm install -g snyk

- name: Scan for Vulnerabilities
  run: snyk test --all-projects
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

## Docker Image Building and Publishing

The workflow handles Docker image building and publishing, which is a common practice for containerized applications. It logs in to Docker Hub securely using GitHub secrets and pushes the Docker image to a repository.

```yaml
- name: Login to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}

- name: Build and Push Docker Image
  run: |
    docker build -t nikitosing/app_python:latest .
    docker push nikitosing/app_python:latest
```
