# Docker Role
This role installs Docker on Ubuntu 20.04

## How to use:
Just use the role, no extra actions required
```main.yaml
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - docker
```


## Requirements:
- Ubuntu 20.04 on machine

