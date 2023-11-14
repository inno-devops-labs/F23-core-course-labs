# Web App Role

Role to deploy app using docker compose. This role uses `docker` role from `roles` to install docker compose and etc.

## Requirements:

- Ubuntu

## Variables to set up:

- `docker_container` : name of container. Default: **my-container**

- `docker_image_name` : name of the docker image to deploy. Default: **nabiull2020/moscow-time-flask-app**

- `docker_image_version` : version of docker image. Default: **latest**

- `internal_port` : container port. Default: **8000**

- `external_port` : host port. Default: **8000**

- `web_app_full_wipe` : flag if wipe is needed. Default: **true**

- `web_app_stop` : flag if stop of compose is needed. Default: **false**

- `app_name` : name of your app. Used to create app folder. Default: **my-app**

## How to use:

Add role to `roles` in playbook:

```
  ...
  roles:
    - docker
```

You can find examples in `ansible/playbooks/dev` folder.

## Wipe:

You can wipe application using such flag whe run playbook:

`--tags wipe_web_app`