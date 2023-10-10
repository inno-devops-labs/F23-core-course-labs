# Web App Role

This is a custom role for deploying the web application. It installs and runs **vladimirka002/innopolis-devops-python-app**
docker image.


## Requirements
Ubuntu 22.04 virtual machine with apt pre-installed (which should be available by default).


## Dependencies

A `docker` role is needed that is created in `/ansible/roles/docker/`.

## Usage

The role can be used just by providing it in the list of roles in yaml config.
```
main.yaml:
- hosts: all
  become: true
  roles:
    - web_app
```

It supports custom parameters that have default values:
* app_name (app_python) - name of the application 
* docker_container (innopolis-devops-python-app) - docker container name
* docker_image_name (vladimirka002/innopolis-devops-python-app) - name of the docker image to deploy and run
* docker_image_tag (latest) - tag of the image
* internal_port (5000) - internal port
* external_port (8000) - external port