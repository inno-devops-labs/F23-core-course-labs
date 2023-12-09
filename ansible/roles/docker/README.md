## Docker Role 

This Ansible role installs pip, Docker

### Requirements: 
* Ubuntu 

### Usage 

Here is an example playbook to use this role:

```shell
- name: Deploy docker
  hosts: all
  become: yes
  become_method: sudo
  roles:
    - docker
```