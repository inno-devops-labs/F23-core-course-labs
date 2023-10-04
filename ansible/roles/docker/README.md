# Docker role

This role installs Docker on Ubuntu 22.04 Jammy according to the official tutorial.

## Requirements:

- Ubuntu 22.04 on machine.

## How to use:

Use the role, no extra actions required.

```
- name: Example of usage the role
  hosts: all
  become: true
  roles:
    - docker
```
