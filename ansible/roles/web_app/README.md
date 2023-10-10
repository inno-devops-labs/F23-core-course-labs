# Ansible Role: Web App

An Ansible Role that runs [this](https://hub.docker.com/repository/docker/sl1depengwyn/python_devops/general) app in docker.

## Requirements

Docker role

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
app_name: app
image_name: sl1depengwyn/python_devops
web_app_full_wipe: false
```

`app_name` is a name of a container.
`image_name` is a name of a docker image.
`web_app_full_wipe` is a boolean value that if true removes app container and image.

## Example Playbook

```yaml
- hosts: all
  roles:
    - web_app
```