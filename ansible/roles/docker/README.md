# Ansible Docker Role

This Ansible role installs and configures Docker on target machines.

## Requirements

- Ansible >= 2.10
- Operating systems:
    - Ubuntu Xenial (16.04)
    - Ubuntu Bionic (18.04)
    - CentOS 7
    - CentOS 8

## Role Variables

Available variables are listed below, along with their default values:

# Docker version to be installed
docker_version: "latest"

# Docker packages to be installed
docker_packages:
  - docker-ce
  - docker-ce-cli
  - containerd.io

# List of Docker users to be added to Docker group
docker_users: []

# Docker daemon configuration options
docker_daemon_config: {}


## Dependencies

None

## Example Playbook

Here is an example playbook to use this role:

- name: Install and configure Docker
  hosts: all
  roles:
    - ansible-docker


## License

MIT

## Author Information

This role was created by Your Name for Your Company.