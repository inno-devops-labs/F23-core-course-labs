# CI

## CI Best Practices

### Multiple jobs
- The workflow contains steps with clear names and dependencies.

### Efficiency
- Build caching is used in-between different steps/runs to ensure efficiency.

- Actions are only triggered when changes are made to `app_python` folder or its corresponding actions with the exception of `.md` files.

### Status badge
- Status in the main README of the repo for visibility.

### Quality gates
- Linting and testing are part of the CI pipeline.

### Vulnerability testing
- Snyk is used to test for vulnerabilities as part of CI, and also makes use of the cache.

### Verify before Push
- Code quality checks (testing, linting) and vulnerability tests and run before publishing the app and will prevent a publish if they fail.

### Secrets
- GitHub secrets are used to store sensitive information.
