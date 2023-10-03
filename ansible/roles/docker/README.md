# Docker role

## Requirements

- Working wm with ubuntu

## Usage

Put following role inside your playbook. Sample:

```
- name: Deploy Docker
  hosts: <your hosts>
  become: true
  roles:
     - docker
```

## Tasks

1. pip installation
2. docker installation
3. docker-compose installation

each task decomposed in the following files and describes inside `tasks/main.yml`
