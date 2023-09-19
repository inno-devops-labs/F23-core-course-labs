# CI/CD Best Practices
1. Caching of PIP - I use venv to accumulate file of deps in known folder and cache it
2. Caching of Docker - I use :buildcache-python tag for that
3. Security check using Snyk
4. Linter produces pretty to read HTML report
5. Results of unit tests are uploaded to GitHub so if somthing failed - information will be displayed in GitHub's dashboard
6. CI triggers only if specifc files are changed
7. Secrets are stored in Github's secrets storage
8. First test - then build