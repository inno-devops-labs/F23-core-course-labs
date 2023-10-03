# Ansible Docker Role

This Ansible role is designed to simplify the installation and setup of Docker on target hosts. It consists of several tasks to ensure Docker and Docker Compose are properly installed.

## Requirements

Before using this role, ensure you have met the following requirements:

- Ansible is installed on your control machine.
- The target host is running a supported Linux distribution.
- All required dependencies are installed.

## Role Variables

This role does not require any specific variables to be set, but you can customize the installation process by modifying the following variables:

- `docker_install_compose`: (default: `false`) Set this to `true` if you want to install Docker Compose.
- `docker_install_compose_plugin`: (default: `false`) Set this to `true` if you want to install Docker Compose plugin(s).

## Example Playbook

Here is an example playbook that uses this Docker role:

```yaml
- hosts: vk_cloud
  roles:
    - role: 'roles/docker-custom-role'
  become: true
```

Make sure to replace vk_cloud with the actual hosts where you want to install Docker.

## Dependencies

This role has the following dependencies:

- geerlingguy.docker: This role relies on the geerlingguy.docker role for installing Docker. You should ensure that this role is available and configured in your Ansible environment.

- geerlingguy.pip: This role also uses the geerlingguy.pip role to install Docker Compose. Make sure to have this role available as well.

You can use:
```
ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.pip
```

## Author Information

This Ansible role was created by Q-Tify.