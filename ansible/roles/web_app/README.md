# Ansible Role: web_app

An Ansible role for deploying a web application using Docker.

## Requirements

- Ansible installed on the control machine
- custom-docker-role available

## Role Variables

Available variables are listed below, along with their default values:

```yml
web_app_full_wipe: false
ports:
  - "80:5000"
image: arseniy5443/moscowtime:latest
allow_duplicates: true
dependencies:
  - role: docker-custom-role
```

## Tags

- install: Tasks for installing the application.
- wipe: Tasks for wiping the application.

## Tasks

### Wipe app
This task is responsible for wiping the application when web_app_full_wipe is true. It performs the following steps:

- Stops the Docker container.
- Deletes the Docker image.
- Removes the compose directory.

### Install App
This task is responsible for installing the application. It performs the following steps:

- Creates a directory if it doesn't exist.
- Creates a Docker Compose file based on the template.
- Runs the application using Docker Compose.

## Templates
- templates/docker-compose.yml.j2: Docker Compose file template.

## Example Playbook
```yml
- name: Deploy the web application
  hosts: web_servers
  roles:
    - role: web_app
      image: arseniy5443/moscowtime:latest
      ports:
        - "80:5000"
      web_app_full_wipe: true
```

## Author Information

Author: Arseniy Rubtsov
