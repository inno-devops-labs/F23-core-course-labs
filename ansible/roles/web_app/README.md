# Web App role

## Best Practices
- Added 2 tasks to deploy and wipe. The tasks are divided into separate executable blocks.
- Dependencies are specified in the meta folder and in this case this is the docker role.
- 2 tags were added: deploy and wipe
- Wipe Logic is implemented to stop if the container is running and clear the data.
- A template was also created for the docker compose configuration file, which is delivered to managed hosts.

## Requirements
Depends on the doker role and uses community.docker.docker_compose, which is included in the standard package with ansible

## Defaults
```sh
image: "bellissimo/devops-inno-daniil-okrug:latest"
container_name: "web_app"
ports: "5000:5000"

deployment_way: "docker_compose" # docker | docker_compose

web_app_full_wipe: true
```

These variables allow you to manage the configuration of the application for deployment.

## Usage
You can add this role to the playbook as it is done below.

```sh
- name: Deploy Web App
  hosts: all
  become: true
  roles:
    - web_app

```