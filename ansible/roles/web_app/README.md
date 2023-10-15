# web_app Ansible Role

## Description

The **web_app** Ansible role simplifies the deployment of a Docker container for your Python application. It automates the process of building and running the container, providing flexibility in configuring container-related parameters.

## Requirements

This role requires the following prerequisites:

- **Docker Role**: Ensure the Docker role is available. You can use the "docker" role from Ansible Galaxy or any other role that sets up Docker on the target machine.

## Role Variables

The role utilizes the following variables, which can be customized in your playbook or inventory:

- `docker_image`: The Docker image to be used for the container. Specify the image name, including the repository if necessary (e.g., `username/repo:tag`).

- `container_name`: The name assigned to the Docker container when created.

- `web_app_port`: The host port mapped to the container.

- `web_app_full_wipe`: A boolean (true/false) indicating whether to perform a full wipe of the container if it already exists.

## Usage

Include this role in your Ansible playbook to deploy your Python application in a Docker container:

```yaml
- hosts: your_target_host
  roles:
    - role: web_app
      docker_image: your-docker-image
      container_name: your-container-name
      web_app_port: 5000
      web_app_full_wipe: true
```

Replace the variables with your specific values. This role will build and run the Docker container for your application.
