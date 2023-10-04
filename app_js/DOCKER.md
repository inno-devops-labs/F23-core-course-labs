# Docker best practices that were implemented:

1. **A lightweight base image**: I am using `node:14-slim` which is a lightweight Node.js image.
2. **Separate application code from dependencies**: by copying `package*.json` first and then installing dependencies, I can leverage Docker's caching mechanism.
3. **Run as a non-root user**: for security reasons, it's a good practice to run the container as a non-root user. I've added a user named `myuser` for this purpose.
4. **Minimize the number of layers**: by minimizing the number of layers, I can reduce the image size.
