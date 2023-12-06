# Best Practices Followed

1.  Using hadolint, a Docker linter.
2.  Using a minimal Docker image (distroless), with recent python put on top of it.

    I tested the images using trivy Docker analysis tool.

    *   *python:3.9-slim-bullseye* has 16 volnerabilities (HIGH: 15, CRITICAL: 1), they come from **debian**.
    *   *distroless/python3:latest* has 29 (HIGH: 25, CRITICAL: 4), as it is rarely updated (specifically the python images).
    *   I will use instead a minimal distroless image, and put a recent python executable on top of it from the official python image. (following [this](https://alexos.dev/2022/07/08/creating-an-up-to-date-distroless-python-image) blog post).
        *   In this case, we only get 3 high severity vulnerabilities (relating to DDoS) from some debain packages, and 0 critical ones. Resulting base image: [DockerHub](nzgeg3s0/python-distroless:3.9-debian11)
3.  Using a multi-stage build process, to reduce the attack surface and size of the final image and avoid needing to delete build tools.
4.  The only binary file executable by the user in the system is python and is owned by root, UNIX tools are not present.
5.  The base image already specifies a USER, I verified that the python process is run by this user by printing the user using `getpass.getuser()` from inside the app, the user is 'monty'.
6.  Only one port is open for the app (port 8000).
7.  Only copying the necessary files for the work of the app (using COPY).
8.  We do not need any docker capabilities to run our app, we can use `--cap-drop=all`.
