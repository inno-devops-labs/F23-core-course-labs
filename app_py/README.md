# README
## Flask application that shows time.
This is Python-written application, Flask framework was used. It shows time and that's it.
This application uses Flask
## Docker
#### How to build:
`docker build . -t my-first-image`
#### How to run:
`docker run -it -p 8000:8000 my-first-image`
#### How to push on DockerHub:
`docker tag <IMAGE ID> ilyamirzazhanov/lab2:<TAG>`
`docker push ilyamirzazhanov/lab2:<TAG>`

##### Docker image with this app is pushed into my DockerHub repository:
https://hub.docker.com/repository/docker/ilyamirzazhanov/lab2/general
