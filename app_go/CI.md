## Best practices used in the GitHub Actions workflow:

- **Caching mechanism**.
To speed up dependency installations, the `actions/setup-go` action is used to cache the Golang dependencies. Subsequent workflows will utilize cache if content of requirements `go.sum` not changed.

- **Using CI variables**.
The workflow uses CI variables to retrieve sensitive information like tokens and usernames from GitHub Secrets, for example `SNYK_TOKEN`. So secrets are not hardcoded in the workflow file and are securely stored.

- **Descriptions on steps and jobs**.
Most of steps and jobs in the workflow is given a descriptive name and comments if needed. This makes it easier to understand the purpose of each step.

- **Using dependend jobs**.
The `docker-build-push-job` job has a `needs` parameter that specifies `[lint-test-job, security-job]`. This ensures that the Docker build and push job will only run if the linting, testing, and security checks have passed successfully.

- **Security checks**:
The `security-job` job uses the Snyk GitHub Action to check codebase for vulnerabilities. The Snyk Action generates a SARIF file with the scan results, which is then uploaded to GitHub Code Scanning.
