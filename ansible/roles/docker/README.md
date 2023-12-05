## Docker Role 

This Ansible role installs pip, Docker, and Docker Compose on Ubuntu systems

## Requirements

Ubuntu 

## Dependencies

None 

## Usage 

Here is an example playbook to use this role:

```
- name: Deploy docker
  hosts: all
  become: yes
  become_method: sudo
  roles:
    - docker
```