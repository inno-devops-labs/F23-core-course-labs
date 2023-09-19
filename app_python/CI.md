## Best practices used in the GitHub Actions workflow:

- **Caching mechanism**.
To speed up dependency installations, the `actions/setup-python` action is used to cache the Python dependencies. Subsequent workflows will utilize pip cache if content of requirements txt's not changed.

- **Using CI variables**.
The workflow uses CI variables to retrieve sensitive information like tokens and usernames from GitHub Secrets, for example `SNYK_TOKEN`. So secrets are not hardcoded in the workflow file and are securely stored.

- **Descriptions on steps and jobs**.
Most of steps and jobs in the workflow is given a descriptive name and comments if needed. This makes it easier to understand the purpose of each step.

- **Using dependend jobs**.
The `docker-build-push-job` job has a `needs` parameter that specifies `[lint-test-job, security-job]`. This ensures that the Docker build and push job will only run if the linting, testing, and security checks have passed successfully.

- **Security checks**:
The `security-job` job uses the Snyk GitHub Action to check codebase for vulnerabilities. The Snyk Action generates a SARIF file with the scan results, which is then uploaded to GitHub Code Scanning.

- **Using pre-commit action**:
The workflow uses the `pre-commit/action` action to run linting tools - `bandit`, `Flake8`, `Black`, `isort`. All tools are already configured in pre-commit, so no need to duplicate configurations in github actions.
