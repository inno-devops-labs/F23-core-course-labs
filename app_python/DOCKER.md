### Docker best practices used in the Dockerfile
* No root user inside
* `--chown=user:user` to copy files into the image with the user ownership
* Use `EXPOSE` to show the container listens on specific network ports at runtime