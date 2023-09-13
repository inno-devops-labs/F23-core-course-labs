# Docker Best Practices

## 1. Use Specific Base Image Tags

- **Best Practice**: Use an official and minimal base image.
- **Implementation**: Utilized the official Node.js image to ensure compatibility and reliability. 
  ```Dockerfile
  FROM node:14-slim
  ```

## 2.  Run as a Non-root User

- **Best Practice**: Avoid running applications inside the container as the root user to enhance security.
- **Details**: When creating a non-root user, it's vital to set proper permissions for directories and files the application might need to access. This action restricts the container from running as root and defines clear boundaries for what the application user can and cannot access.
- **Implementation**: In the Dockerfile, a new user `appuser` is created, given ownership of the `/app` directory, and then set as the current user.
  ```Dockerfile
  RUN useradd --create-home appuser && chown -R appuser:appuser /app
  USER appuser
  ```

## 3. **Copy Only Necessary Files**

- **Best Practice**: Minimize the image size and potential security vulnerabilities by copying only required files.
- **Implementation**: Copied only the `package.json`, `package-lock.json` (or `yarn.lock`), and the application code. Optionally, a `.dockerignore` file can be used to ensure unnecessary files are not added to the Docker context.
  ```Dockerfile
  COPY package*.json ./
  COPY . .
  ```

## 4. **Handle Cache Efficiently**

- **Best Practice**: Utilize Docker's layer caching mechanism to speed up builds and reduce redundant operations.
- **Implementation**: Copied `package.json` and installed dependencies before copying the rest of the app code to utilize cache when dependencies don't change.
  ```Dockerfile
  COPY package*.json ./
  RUN npm install
  COPY . .
  ```

## 5. **Health Checks**

- **Best Practice**: Implement health checks to ensure the containerized application is running as expected.
- **Implementation**: Used `curl` to periodically check the application's endpoint.
  ```Dockerfile
  HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:3000/ || exit 1
  ```

## 6. **Reduce Image Size**

- **Best Practice**: Minimize the Docker image size to speed up deployment and reduce attack vectors.
- **Implementation**: Used a slim version of the Node.js image and removed unnecessary files or caches. The use of multi-stage builds can further reduce image size.

## 7. **Environment Variables**

- **Best Practice**: Use environment variables for configuration that might change between deployments.
- **Implementation**: For a React app, environment variables can be passed during the build or run phase to adjust configurations. This ensures flexibility and avoids hardcoding values in the Docker image.
