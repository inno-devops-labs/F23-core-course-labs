# Ansible Role: Docker

This Ansible role is designed to automate the installation and setup of Docker on Ubuntu-based systems. It also installs the Docker module for Python, allowing you to manage Docker containers and images using Ansible.

## Requirements

- Target hosts should be running an Ubuntu-based Linux distribution.
- Ansible should be installed on the control machine.

## Role Variables

This role does not require any specific variables to be defined. However, you can customize the Docker version or other parameters by modifying the tasks in `tasks/main.yml`.

## Dependencies

None

## Example Playbook

To use this role in your playbook, include it in your playbook's `roles` section, like this:

```yaml
---
- hosts: your_target_hosts
  become: true
  roles:
    - docker
