# Docker installation role
This role is designed for the seamless installation of Docker on Ubuntu 22.04 Jammy, following the official instructions.

## Prerequisites:
The target system must be running Ubuntu 22.04.

## Usage:
To use this role, simply include it in your playbook. There's no need for any additional configurations.

```
- name: Implementing the Docker role
  hosts: all
  become: yes
  roles:
    - docker
```