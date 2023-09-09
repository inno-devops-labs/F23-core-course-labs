# Docker best practices

Azamat Shakirov B20-CS

a.shakirov@innopolis.university



#### **Use Official and Verified Images**

The base image used in this Dockerfile is `python:3.9-slim`. This is the official Python runtime image, which provides a minimal version of Python 3.9.

#### Minimize the image size

The use of the `slim` variant of the base image helps to minimize the size of the resulting Docker image. Additionally, the `--no-cache-dir` flag is used with `pip install` to avoid caching package downloads, reducing the image size further.

#### Use a separate user

A new user named `pythonuser` is created with the `useradd` command. This helps improve the security of the container by running the application as a non-root user. The ownership of the `/home/pythonuser` directory is also changed to the `pythonuser` user.

#### Use a working directory

The `WORKDIR` instruction sets the working directory inside the container to `/home/pythonuser/app`. This is where the application code and requirements file will be copied.

#### Copy the application code and requirements

The `COPY` instructions are used to copy the `requirements.txt` file and the `main.py` file into the Docker image.

#### Install the required Python packages

The `pip install` command is used to install the Python packages specified in the `requirements.txt` file. The `--no-cache-dir` flag is used to avoid caching package downloads, reducing the image size.

#### Switch to the new user

The `USER` instruction is used to switch the user to `pythonuser`. This ensures that the application is run with the least privileged user, improving security.

#### Linter

[Hadolint](https://hadolint.github.io/hadolint/) Docker Linter was used for this Dockerfile. `Hadolint` is a tool that helps validate Dockerfiles and provides suggestions for improving their quality, security, and efficiency. 