# Web App Role
This role install web application to the target

## Requirements:
- Docker installed on target

## How to user:
Just use the role, no extra actions required
```main.yaml
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - web_app
```