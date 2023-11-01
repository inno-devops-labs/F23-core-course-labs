# Docker Role

## Requirements
Requires a pre-installed apt package manager for target machines.

## Vars
Docker role variables:
```sh
docker_compose_version: "1.29.2"
docker_version: "5.0.3"
```

## Tasks
Tasks performed for installing and deploying Docker:

- Install pip
- Install docker
- Install docker-compose