# Docker Ansible Role

## Description

The Docker Ansible role automates the installation and setup of Docker on a target host. Docker is a versatile platform for developing, shipping, and running applications within containers. This role simplifies the process of installing Docker and Docker Compose, making it easier to manage containerized applications on your infrastructure.

## Requirements

Before using this role, ensure that the following requirements are met:

### Supported Platforms

This role is designed to work on Linux-based systems, including:

- Ubuntu
- Debian

### Dependencies

This role does not have external role dependencies. However, ensure that your target host meets the following prerequisites:

- A working package manager (apt or yum depending on the platform).
- Internet connectivity to download Docker packages.

## Role Variables

This role provides several variables that you can set in your playbook to customize the Docker installation:

- `docker_version` (default: "24.0.5"): Set the Docker version to be installed.

- `compose_version` (default: "1.29.2"): Set the Docker Compose version to be installed.

## Usage

To use this role in your Ansible playbook, follow these steps:

1. Create an inventory file with the target host(s) where you want to install Docker.

2. Include this role in your playbook, specifying the required variables (if needed). For example:

    ```yaml
    - name: Install Docker
      hosts: my_target_hosts
      become: yes
      roles:
        - role: docker
          docker_version: "20.10.7"
          compose_version: "1.27.0"
    ```

3. Run your playbook using the `ansible-playbook` command:

    ```bash
    ansible-playbook your-playbook.yaml -i your-inventory.ini
    ```

This will execute the role on the target host(s), ensuring that Docker and Docker Compose are installed with the specified versions.
