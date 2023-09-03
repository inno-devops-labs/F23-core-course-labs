# Docker Security Best Practices
- Root user is used only for package installation, all other operations including application running are done on local user.
- Smallest base image which is enough to run the application.
- Multistage for testing and production deployment.
- Docker scout is used for vulnerability scanning(in the dockerhub registry).
- Hadolint linter for Dockerfile(https://hadolint.github.io/hadolint/).