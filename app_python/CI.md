## CI best practices

1. **Separate jobs pipeline** Each process is separated and run independently from the others. It helps easily determine the failing step of the workflow.
2. **Caching**: caching dependencies allows to optimize downloads and installations by using needed dependencies already in cache.
3. **Docker image upload:** docker image is automatically uploaded to dockerhub when a change is pushed and all checks are successfull.
4. **Timeout for jobs**: I added a timeout for each job so it will be terminated in case of long execution.
5. **Path filters**: The workflow is launched only when changes are pushed to a certain path.
