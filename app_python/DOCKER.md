# Docker Best Practices

## Avoid Root Permission
Docker creates simpleuser with no password and continue work as simpleuser. 

## Dockerignore
To exclude files not relevant to the build, without restructuring your source repository, use a .dockerignore file.

## Multi-stage build
Multi-stage builds allow to drastically reduce the size of your final image, without struggling to reduce the number of intermediate layers and files.

## Using pipes
Use && or || in RUN command to minimize docker layers.

## EXPOSE
EXPOSE indicates the ports on which a container listens for connections. 

## COPY instead ADD
COPY only supports the basic copying of local files into the container, while ADD has some features (like local-only tar extraction and remote URL support) that are not immediately obvious.

## Set working directory
It set working directory for clarity and reliability.

## Use ENTRYPOINT
The best use for ENTRYPOINT is to set the image's main command, allowing that image to be run as though it was that command.
