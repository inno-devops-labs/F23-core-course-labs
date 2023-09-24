# Docker best practices that were implemented:

1. **Base image**: I used the `python:3.9-slim` image which is a lightweight version of the Python image, reducing the potential attack surface.

2. **Environment variables**: 
   - `PYTHONDONTWRITEBYTECODE`: it prevents Python from writing pyc files to disc (prevents Python from writing the bytecode).
   - `PYTHONUNBUFFERED`: it ensures that Python output is sent straight to terminal and makes it easier to monitor the logs of the application.

3. **No root user**: I created a non-root user (`myuser`) and switched to this user for running the application. This is a security best practice to ensure that potential attackers cannot gain root privileges inside the container.

4. **Minimal install**: I used the `--no-install-recommends` flag with `apt-get` to ensure only the necessary packages are installed, reducing the image size and potential attack surface.

5. **Clean up**: After installing packages with `apt-get`, I cleaned up to reduce the image size.

6. **Explicit port exposure**: I explicitly set the port for the application to run on - `8000`.

7. **Immutable image**: by copying only the necessary files and setting environment variables, I ensure the image is immutable, meaning it doesn't change and can be reliably moved across environments.
