[![Go](https://github.com/IlyaMirzazhanov/core-course-labs/actions/workflows/go_ci.yml/badge.svg)](https://github.com/IlyaMirzazhanov/core-course-labs/actions/workflows/go_ci.yml)
# Go Web App

This web application is written on Go programming language. 

Main advantages of Go:
* Simple - syntax is intuitive and easy to learn
* Secure - code is error-secured
* Effective - achieves the goal
* Fast - execution time is food

## Docker
#### How to build:
`docker build . -t go-image`
#### How to run:
`docker run -it -p 3000:3000 go-image`
#### How to push on DockerHub:
`docker tag <IMAGE ID> ilyamirzazhanov/lab2:<TAG>`
`docker push ilyamirzazhanov/lab2:<TAG>`

## Docker multi-stage builds
Docker Multi-Stage Builds is a feature introduced by Docker that allows for a more efficient and streamlined build process when creating Docker images. 

With multi-stage builds, one can use multiple "stages" within a single Dockerfile, where each stage represents a phase of the build process. Each stage can be based on a different base image and can include the necessary dependencies and tools required for that specific phase.

My simple application will not gain much using this technology. 

##### Docker image with this app is pushed into my DockerHub repository:
https://hub.docker.com/repository/docker/ilyamirzazhanov/lab2/general

# Unit Tests
* Testing web app on validity
* Code simple and fast
* Uses standart Go testing module
