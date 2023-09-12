# Docker Best Practices in the Project - Daniil Okrug

1. Rootless container. A separate user is created in the container and given access to run the program.

2. Restricting user rights in the container. The owner of the files is root, but another user with normal access rights runs it. The basic idea is that the new user can only execute the files passed to him.

3. Multi-stage build. Dockerfile build consists of 2 steps. Stage 1 includes copying necessary files from the root side and in the second stage a user is created, files with restricted access are copied for him and the application is launched.

4. To optimize the Docker image, only the most necessary files are copied inside.