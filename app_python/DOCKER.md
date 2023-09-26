### Best practices used
1. **Using Official Base Image:** The Dockerfile starts with an official Python base image (`python:3.10-slim`), following the best practice of using trusted base images.

2. **Creating a Non-Root User:** A non-root user (`nonrootuser`) and group (`usergroup`) are created, adhering to the best practice of running processes with reduced privileges for enhanced security.

3. **Setting the Working Directory:** The `WORKDIR` instruction sets the working directory to `/app_python` to improve clarity and organization.

4. **Combining Package Management Commands:** The `apt-get` commands for updating the package index, installing packages, and cleaning up are combined into a single `RUN` instruction, reducing the number of image layers and improving image efficiency.

5. **Changing Ownership of Application Directory:** Ownership of the `/app_python` directory is changed to the non-root user (`nonrootuser`), ensuring the user has proper permissions to access application files.

6. **Switching to the Non-Root User:** The `USER` instruction switches to the non-root user (`nonrootuser`) for added security during container execution.

7. **Copying Requirements File Separately:** The `COPY` command copies the `requirements.txt` file separately, allowing Docker to cache dependencies and optimize build efficiency.

8. **Installing Python Packages with Caching Disabled:** The `pip install` command installs required Python packages with caching disabled using the `--no-cache-dir` option, reducing image size and preventing potential caching issues.

9. **Copying the Application Code:** The application code is copied into the container, ensuring that the necessary files are available for execution.

10. **Exposing the Necessary Port:** The `EXPOSE` instruction documents that the container will listen on port 5000.

11. **Setting Environment Variables:** Environment variables for the Flask application (`FLASK_APP` and `FLASK_RUN_HOST`) are set to configure the application correctly.

12. **Using CMD for Flexibility:** The `CMD` instruction is used instead of `ENTRYPOINT`, providing flexibility for users to customize the container's behavior when running it.