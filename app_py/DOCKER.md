# Docker usage.

## Best Docker practices:
* No root user inside, in Dockerfile I created new user under which I run image
* Rational usage of Dockerfile
* Using `-rm` when launching container, so they're not littering memory
* Pushing image on DockerHub
* Used WORKDIR inside Dockerfile
* Used COPY instead of ADD
