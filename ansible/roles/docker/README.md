# Ansible Docker role

The role installs `pip`, `docker` and  `docker-compose` as it was required by the home assignment.

## Requirements
No special requirements are needed except having ubuntu and ansible installed on you machine.

## Usage
To use the role, one needs to specify it in roles section in his/her playbooks. Something like the following:

```
- name: <some_name>
  hosts: <some_host>
  become: yes
  roles:
    - docker
    
```