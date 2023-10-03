# CI Best Practices

**Run tests** – there is a testing job for all pushes and MR to master.

**Ensure software quality** – apart from tests, there are also linter and vulnerability check jobs

**Optimize build steps** – all logically separate units of work are split into separate reproducible steps and jobs

**Optimize build through caching** – no external dependencies are used in the project 

**Ensure pipeline security** – sensitive data like Dockerhub token is stored as encrypted in GitHub Secrets storage.

