### Best practices:
* Rootless container
* Use optimal base image (do not use alpine for python base image https://pythonspeed.com/articles/base-image-python-docker-images/)
* Do not use tag `latest`
* Use `COPY` instead of `ADD` wherever possible
* Use exec-form for `ENTRYPOINT`
* Copy only needed files inside the container