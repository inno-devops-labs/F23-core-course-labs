# Docker Ansible Role

This Ansible role is designed to simplify the installation and management of Docker on your target hosts. It provides flexibility and customization options to suit different use cases and operating systems.

## Role Variables

### Docker Edition and Packages

Specify the Docker edition (Community Edition 'ce' or Enterprise Edition 'ee') and the packages to be installed:
```yaml
docker_edition: 'ce'
docker_packages:
  - "docker-{{ docker_edition }}"
  - "docker-{{ docker_edition }}-cli"
  - "docker-{{ docker_edition }}-rootless-extras"
  - "containerd.io"
docker_packages_state: present
```

### Docker Service Configuration

Control the Docker service with these options:
```yaml
docker_service_manage: true
docker_service_state: started
docker_service_enabled: true
docker_restart_handler_state: restarted
```

### Docker Compose Plugin

Install the Docker Compose plugin:
```yaml
docker_install_compose_plugin: true
docker_compose_package: docker-compose-plugin
docker_compose_package_state: present
```

### Docker Compose

Configure Docker Compose installation (optional):
```yaml
docker_install_compose: false
docker_compose_version: "v2.11.1"
docker_compose_arch: "{{ ansible_architecture }}"
docker_compose_url: "https://github.com/docker/compose/releases/download/{{ docker_compose_version }}/docker-compose-linux-{{ docker_compose_arch }}"
docker_compose_path: /usr/local/bin/docker-compose
```

### Repository Setup

Enable or disable Docker repository setup:
```yaml
docker_add_repo: true
```

Specify Docker repository settings for various Linux distributions:
```yaml
docker_repo_url: https://download.docker.com/linux
docker_apt_release_channel: stable
docker_apt_ansible_distribution: "{{ 'ubuntu' if ansible_distribution in ['Pop!_OS', 'Linux Mint'] else ansible_distribution }}"
docker_apt_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64' }}"
docker_apt_repository: "deb [arch={{ docker_apt_arch }} signed-by=/etc/apt/trusted.gpg.d/docker.asc] {{ docker_repo_url }}/{{ docker_apt_ansible_distribution | lower }} {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
docker_apt_ignore_key_error: true
docker_apt_gpg_key: "{{ docker_repo_url }}/{{ ansible_distribution | lower }}/gpg"
docker_apt_gpg_key_checksum: "sha256:1500c1f56fa9e26b9b8f42452a553675796ade0807cdce11975eb98170b3a570"
docker_apt_filename: "docker"

docker_yum_repo_url: "{{ docker_repo_url }}/{{ (ansible_distribution == 'Fedora') | ternary('fedora','centos') }}/docker-{{ docker_edition }}.repo"
docker_yum_repo_enable_nightly: '0'
docker_yum_repo_enable_test: '0'
docker_yum_gpg_key: "{{ docker_repo_url }}/centos/gpg"
```

### Users in Docker Group

List users to be added to the Docker group:
```yaml
docker_users: []
```

### Docker Daemon Options

Customize Docker daemon options using a dictionary:
```yaml
docker_daemon_options: {}
```

## Example Playbook

Here's an example of how to use this role in an Ansible playbook:

```yaml
---
- name: Install Docker
  hosts: your_target_hosts
  become: true
  roles:
    - docker
```
