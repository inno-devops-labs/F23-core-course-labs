## Here are best practices that I employed within the Dockerfile:

1. Specify a specific version for the base image: Use a specific version of the base image, rather than just using "latest". 

2. Use a meaningful working directory: Setting the working directory to "/app" using the `WORKDIR` instruction makes it easy to manage files within the container. 

3. Copy only necessary files: The `COPY` instruction is used to add the "main.go" file to the "/app" directory inside the container.
 
4. Expose the required ports: In this case, the `EXPOSE` instruction exposes port 8008 from inside the container. 

5. Use the CMD instruction for runtime actions: The `CMD` instruction specifies the command to be run when the container starts. 



# To build
```
docker build -t wildqueue/devops-hw-golang:tagname .
```

# To run
```
docker run -p 8008:8008 --user 1001 app_python
```