# Continuous Integration Workflow

This document describes the Continuous Integration (CI) workflow of this project and the best practices applied to optimize it. The workflow is managed with GitHub Actions and is defined in the `.github/workflows/python-ci.yml` file.

## Workflow Description

The CI workflow is triggered whenever there's a push or pull request to the `main` branch. It includes several steps:

1. **Checkout**: Checks out the repository's code.
2. **Set up Python**: Sets up a Python environment with a specific version (3.8 in this case).
3. **Cache pip dependencies**: Caches the pip dependencies to speed up the workflow.
4. **Install dependencies**: Installs the project dependencies.
5. **Lint with flake8**: Runs the flake8 linter on the Python code.
6. **Test with pytest**: Runs the pytest tests.
7. **Login to DockerHub**: Logs in to DockerHub using the username and access token stored in GitHub secrets.
8. **Build and push Docker image**: Builds a Docker image from the Dockerfile in the repository and pushes it to DockerHub.
9. **Run Snyk to check for vulnerabilities**: Checks for vulnerabilities in the project with Snyk.

## Best Practices

The following best practices are applied in the CI workflow:

1. **Use actions instead of inline scripts**: Actions are used instead of inline scripts to mitigate injection attacks. This is considered a best practice for security reasons.
2. **Use specific version tags for actions**: Specific version tags are used for actions to prevent the workflow from breaking if the action authors introduce breaking changes in newer versions.
3. **Limit the permissions of the GITHUB_TOKEN**: The permissions of the GITHUB_TOKEN are limited to prevent potential attacks.
4. **Cache build dependencies**: The `actions/cache` action is used to cache pip dependencies and speed up the workflow.
5. **Monitor and measure your pipeline**: The status and results of the workflow are monitored and measured for continuous improvement.
6. **Amplify feedback**: The ability to amplify feedback is built into the workflow. This helps to quickly construct new knowledge and make it explicit throughout the organization.

The implementation of these best practices helps to ensure the efficiency, reliability, and security of the CI workflow.

![Python CI](https://github.com/Aisinus/core-course-labs/actions/workflows/python-ci.yml/badge.svg)
