# CI/CD Best Practices
1. To store dependencies in a designated folder and cache them, I utilize venv for PIP caching.
2. For Docker caching, I employ the :buildcache-python tag.
3. Snyk is used to perform security checks.
4. The linter generates an HTML report that is easy to comprehend.
5. Unit test results are uploaded to GitHub to enable the display of failure information on the dashboard.
6. Continuous integration is initiated only when specific files are modified.
7. Confidential information is kept in Github's secret storage.
8. The build process follows the testing phase.