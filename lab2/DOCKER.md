# Dockerfile description

## Building image

```bash
docker build -t <image_name> .
```

## Running the Docker Container

```bash
docker run -p 5000:5000 <image_name>
```

##  Best practices used in Dockerfile

1. All build and install step are moved up

2. Used EXPOSE keyword to highlight which port should be opened

3. Docker application started not from root user. User created during build