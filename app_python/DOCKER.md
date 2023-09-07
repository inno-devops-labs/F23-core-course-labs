# Docker Best Practices

In this project, we follow these best practices to ensure secure, efficient, and a maintainable Docker image.

1. **Use Official Base Images:**  python:3.10.

2. **Set Working Directory:**  `WORKDIR`.

3. **Separate Dependencies:** Install dependencies before copying code.

4. **Copy Only Necessary Files:** `COPY`.

5. **Limit Permissions:** Use non-root user.

6. **Multi-Stage Builds:** Multi-stage builds for smaller images.

7. **Avoid Hardcoding:** Use secrets for sensitive data.
