# Docker Best Practices

In this section, I'll describe the best practices employed within the Dockerfile for containerizing the web application.

1. Use a Minimal Base Image

    I used the `nginx:alpine` base image, which is a lightweight and minimalistic image based on Alpine Linux. This choice reduces the image size and minimizes security vulnerabilities.

2. Set a Working Directory

    I set the working directory to `/usr/share/nginx/html` to ensure that all commands run within the appropriate context within the container.

3. Copy Necessary Files

    I copy the `index.html` file into the container. This file represents the content of the web application. I copy only necessary file, this minimizes the image size and avoids copying unnecessary files.

4. Expose Ports

    In this case, I haven't explicitly specified an `EXPOSE` instruction because NGINX by default listens on port 80, which is exposed.

5. Define the Startup Command

    The CMD instruction specifies the command to start NGINX in the foreground, ensuring that it runs as the main process within the container.

6. Limit Resource Usage

    Docker allows you to set resource limits for containers, preventing them from using too much memory and CPU. This ensures efficient resource utilization and enhances security against resource-intensive attacks.
