# Web App Role
This role install web application with given docker image onto the host

## Requirements:
- Docker role available

## How to user:
```main.yaml
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - role: web_app
      image: ubuntu:latest
      ports:
        - 1337:322
        - 2000:3000
```