# Docker Role

## Requirements
This Docker role has the following requirements:
- Pre-installed apt package manager on target machines.

## Variables
The Docker role includes the following variables:
docker_compose_version: "1.29.0"
docker_version: "6.0.0"


## Tasks
The following tasks are performed for installing and deploying Docker:

1. Install pip
2. Install Docker
3. Install Docker Compose