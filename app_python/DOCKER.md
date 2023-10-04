# Docker

## Best practices
1. Rootless container. Creating a non-root user to run the application inside the container 
minimizes potential security risks.
2. Alpine Base Image. I used `python:3.8-alpine` base image instead of the standard python:3.8.
Alpine images are known for their smaller size, which results in significantly reduced image sizes and faster deployments.
3. Explicit Port Exposure. I explicitly specified the port that the application listens to by using the `EXPOSE` directive.
This enhances container readability and provides a clear indication of the exposed service port.
4. Organized Source Code. I placed the application's source code in a dedicated `app` folder, which is then copied into the image.
This practice ensures that only essential application files are included in the resulting image, avoiding unnecessary files like READMEs or backups.
5. Consolidated RUN Directives. To optimize image layering and minimize the number of layers, I combined multiple adjacent `RUN` commands into a single instruction. 
This reduces the overall image size and enhances build efficiency.
6. Dependency Caching. Place files that are less likely to change first. In my Dockerfile, I first copy `requirements.txt` and then the rest of the code.
Since the dependencies do not change often, docker will use cached requirements most of the time when building image.