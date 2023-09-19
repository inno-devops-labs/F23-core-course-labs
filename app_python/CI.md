## Best practices
1. When authenticating to Docker Hub with GitHub Actions, use a personal access token
2. Utilize build cache to enhance workflow efficiency
3. Workflow run only when changes occur in the app_python folder
4. Job `docker` runs only when job `build-and-test` is successful
5. Using variables