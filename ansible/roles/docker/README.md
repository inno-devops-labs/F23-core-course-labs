# Docker Role
This role installs Docker on Ubuntu 22.04 Jammy according to official tutorial

## Requirements:
- Ubuntu 22.04 on machine

## How to user:
Just use the role, no extra actions required
```main.yaml
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - docker
```