This role provides configurable deployment of a docker container of a simple web app.
Tested with Ubuntu 20.04, 22.04

## Requirements

None.

## Variables

See `defaults/main.yml` for full list of variables.

Use `app_docker_image` to specify docker image.

Use `app_port` to specify exposed port of app container.

Use `app_container_name` to specify Docker container name.

Set `app_wipe` to true to wipe the app and associated files.

## Tags

Use `pull` tag, to only perform the pull of the image.

Use `deploy` tag to perform/wipe deployment of the image.

Use `docker_compose` tag to add/wipe docker-compose.yml.

## Dependencies

docker role.

## Example Playbook

```yaml
- name: Deploy Dockerized app
    hosts: vms
    become: yes
    become_method: sudo
    roles:
    - web_app
```
