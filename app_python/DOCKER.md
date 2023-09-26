# Docker best practices

## 0. I considered Multistage builds in app_javascript/DOCKER.md

## 1. Rootless containers, run as non root
I create a non-root user myuser to run the application, adhering to the principle of not running containers as the root user.

## 2. Use trusted base images + small size alpine
I used official lightweight python image based on alpine.

## 3. Don’t bind to a specific UID
In my Docker containerization practices, I always adhere to the principle of not binding to a specific UID. This practice ensures that my containers remain flexible and portable across different environments. By avoiding hardcoding specific UIDs within my containerized applications, I enable them to run seamlessly on various host systems without encountering permission issues or conflicts.

## 4. Efficient Dependency Management in Docker Containers
Firstly, I utilize the COPY instruction to transfer the requirements.txt file from the host system into the Docker container, ensuring an up-to-date record of necessary packages and their versions. Subsequently, I employ the RUN instruction to execute the pip install -r requirements.txt command within the container. This method not only streamlines dependency installation but also leverages Docker's caching mechanism.

## 5. Make executables owned by root and not writable
I applied this practice because it enhances security by preventing unauthorized modifications to essential files, aligning with Docker's security principles and safeguarding the integrity of my containerized applications.

## 6. Exposed ports
I applied the "EXPOSE" instruction in Docker which involves explicitly specifying the network ports that a containerized application is designed to listen on within the container. This practice enables better network communication between containers and the host system, making it easier to manage and secure network connections, while also providing valuable documentation to users about the container's intended network interface.

## 7. Credentials and confidentiality
I don't hardcode sensitive data directly into Docker images or Dockerfiles, as these can be easily exposed and compromised.

## 8. COPY
I used COPY instead of ADD according to Dockerfile best practices.

## 9. .dockerignore
I created a .dockerignore file in your project directory to specify patterns of files and directories that should be excluded from the build context to reduce image from useless files.

## 10. Linting
I use Hadolint linter. It is a fast and simple Dockerfile linter that checks for best practices and common mistakes in Dockerfiles.

## 11. Include health / liveness checks
I implemented the practice of healthchecking. These checks involve implementing mechanisms within the containerized application to continuously monitor its health and responsiveness, ensuring it remains available and reliable, while also allowing container orchestration platforms to make informed decisions about container placement and scaling.

## 12. WORKDIR
I used WORKDIR to setup working directory. Moreover, I used absolute paths.