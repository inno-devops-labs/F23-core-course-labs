# Implemented Docker Best Practices

## 1. Use an Official Base Image

Start with an official elixir runtime as a parent image from Docker Hub. This ensures that we are using a trusted and maintained base image.

```Dockerfile
FROM hexpm/elixir:1.14.5-erlang-25.3.2.4-alpine-3.18.2 AS builder
```
Use multistage build

## 2. Set Environment Variables

Set environment variables within the Dockerfile.

```Dockerfile
ENV MIX_ENV=prod
ENV PORT=4000
```

## 3. Create a Working Directory

Create a working directory inside the container, and set it as the current working directory. This is where your application code will be copied.

```Dockerfile
WORKDIR /app_elixir
```

## 5. Use mix.lock

mix.lock ensures hash checking of the deps. 

```Dockerfile
COPY mix.lock ./

RUN mix local.hex --force
RUN mix do deps.get, local.rebar --force, deps.compile
```

## 6. Use .dockerignore file

Here it's not needed since I copied only necessary folders

# Security best practices


## 1. Avoid root run

```Dockerfile
# Add new non-root user
RUN useradd defaultuser

# Use this user to make container root-less
USER defaultuser
```

## 2. Default non-root user has only executable permissions for binaries

defaultuser aren't able to write binaries since it's owner by root

## 4. Expose only one necessary port

## 5. Use COPY/ADD wisely

Use COPY since it's more friendly

## 6. Lint Dockerfile via hadolint

```bash
$ brew install hadolint
$ hadolint Dockerfile
```
