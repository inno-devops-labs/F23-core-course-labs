# Docker Role

This role installs Docker on Ubuntu 22.04 according to official tutorial.

## Requirements

- Ubuntu 22.04 on machine

## How to use

```main.yaml
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - docker
```
