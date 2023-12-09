# Docker Best Practices:

- Opt for using podman instead of docker, as it offers the following advantages:
  - It does not require root privileges to run.

  - No need for a daemon to be running.

- Utilize rootless containers to enhance security and avoid unnecessary privileges.

- Cache dependencies in separate Docker steps to optimize the build process.

- Implement multi-stage builds to reduce the final image size.

- Select a minimal busybox image as the base image for Rust applications.

- Utilize .dockerignore to exclude unnecessary files from the containers.

- Minimize the number of layers in the Dockerfile, such as grouping apt install and pip install commands.

- Remove caches from package managers to reduce image size.

- Prefer using COPY instead of ADD when network capabilities are not required.
