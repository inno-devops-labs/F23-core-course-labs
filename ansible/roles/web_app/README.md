# The `web_app` Ansible role

An Ansible role for deploying a web application using Docker and Docker Compose

## Requirements

This role requires the following dependencies:

- Docker API >= 1.25
- Docker SDK for Python >= 1.8.0
- PyYAML >= 3.11
- docker-compose >= 1.7.0


## Dependencies

This role is dependent on `docker` role

## Variables

The following variables can be customized to configure your web application deployment:

- wipe: A boolean variable that determines whether to wipe all related files when running the playbook. True by default.

## Tags

This role includes the following tags:

- web_app: Includes all tasks related to deploying the web application.
- web_app_wipe: Includes all tasks related to wiping the web application.

## Usage

To use this role, include it in your playbook and customize the necessary variables:

```yaml

- hosts: vm
  roles:
  - role: web_app
    vars:
      wipe: true
```

You can also run specific tasks using tags:

```bash
ansible-playbook playbook.yml --tags "web_app_wipe"
``````
