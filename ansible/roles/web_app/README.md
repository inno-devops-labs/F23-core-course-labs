# Application deployment role

This Ansible role is used to deploy a web application on a remote host.
It utilize Docker custom role to install Docker, and then runs the application using Docker Compose.

## Requirements

- Ansible, tested on version [core 2.14.3].
- A Unix-like operating system on the target system, tested on Ubuntu.

### Install dependencies

All roles dependencies located in `ansible/requirements.yml`. To install them, use command inside `ansible` directory:
```
ansible-galaxy install -r requirements.yml
```
Dependencies include custom docker role, and its dependencies (geerlingguy.docker, geerlingguy.pip).

## Role Variables

Role variables are located in `ansible/roles/web_app/defaults/main.yml`. They are used to configure the application deployment.
Variables are:
`service_name` - name of the service, used to name containers on the host.
`image_name` - name of the image to pull from Docker Hub.
`host_port` - port on the host to expose the application.
`internal_port` - internal port of the application inside the container.
`web_app_full_wipe` - if set to `true`, will clean up all containers and images on the host. (default: `true`)

## Usage

To use this role, include it in your playbook like that:
```
- name: Deploy Python web application
  hosts: devopscourse
  become: true
  roles:
    - role: web_app
      service_name: timeapp_python
      image_name: vladspigin/timeapp:latest
      host_port: 80
      internal_port: 8080
```

Tags available for this role:
- `deploy` - deploy the application.
- `wipe` - clean up all containers and images on the host.

## Dynamic inventory
If you want to use yandex cloud dynamic inventory, you can add use `yacloud_compute.yml` inventory and you should rename `yacloud_key.example` wirh `yacloud_key` with actual credentials.
