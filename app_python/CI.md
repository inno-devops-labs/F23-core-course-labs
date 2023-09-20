# CI/CD Best Practices
1. I used `actions/setup-python` for set up python environment
2. Dependencies caching for poetry using `cached-poetry-dependencies`
3. Vulnerability check using the Snyk action. This helps identify and address potential security issues.
4. Linting check using pylint
5. Unit tests using pytest

