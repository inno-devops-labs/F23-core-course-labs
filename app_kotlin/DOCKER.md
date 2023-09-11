### Best practices:
* Rootless container
* Use optimal base image (do not use alpine for python base image https://pythonspeed.com/articles/base-image-python-docker-images/)
* Do not use tag `latest`
* Use `COPY` instead of `ADD` wherever possible
* Use exec-form for `ENTRYPOINT` 
* Copy only needed files inside the container
* User multi-stage build for kotlin spring boot app. Firstly, we build app and generate .jar file. Then copy this file to main container