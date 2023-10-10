# web_app role

This role deploys app with help of docker image on host machine.

## Requirements

- Docker role on host

## How to use

```main.yaml
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - role: web_app
      image: <name_of_image>:<tag>
      ports:
        -<some_port>:<some_port>
        ...
```
