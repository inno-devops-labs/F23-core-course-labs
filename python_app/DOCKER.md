I have employed several best practices in the Dockerfile provided above. Let's elaborate on each of them:

1. Using official base image `python:3.9-slim`.

2. The container implies non-root user is used. 
   
3. Directory structure is maintained.

4. Using `requirements.txt` to properly install all the required libraries.

5. Running tests as they allow to pre-check the correctness of the project.

6. Exposing the port to minimize security problems with connections.

7. Using CMD with exec to easily start the project.