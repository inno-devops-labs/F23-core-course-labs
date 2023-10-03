# Custom Docker Role

This Ansible role installs Docker using apt and Docker Compose via pip on a target system. It also installs pip itself, and updates apt.

## Requirements

- Ansible, tested on version [core 2.14.3].
- A Unix-like operating system on the target system, tested on Ubuntu.

### Install dependencies

All roles dependencies located in `ansible/requirements.yml`. To install them, use command inside `ansible` directory:
```
ansible-galaxy install -r requirements.yml
```

## Role Variables

- `docker_install_compose` and `docker_install_compose_plugin`: Defaults to `false`. So, Docker Compose will not be installed using apt.

## Usage

To use this role, include it in your playbook like that:
```
- name: lab5
  hosts: yandex_vms
  become: true
  roles:
    - docker_custom
```
