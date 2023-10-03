# Custom Docker role

## Description and requirements
### Deps
- `geerlingguy.pip`  
- `geerlingguy.docker`
- Only for Debian-based GNU/Linux distribution
### Description
This role stands for deployment of docker and docker-compose to the targeted hosts with all required dependies, this role also turning on docker daemon and genneraly prepare target host os to run docker containers and build infrastructure of multi-docker containers with docker-compose utilization

## Usage
- Utilize this role by installing deps and adding it into your playbook, nothing in addition required
- Example of playbook usage:
```
- name: ansibleLab5
  hosts: all
  become: true
  roles:
    - docker
```