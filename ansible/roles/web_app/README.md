Web app
=========

Ansible role which deployes stateless standalone web application using docker-compose

Role Variables
--------------


| Variable                | Description                                                                        | Default                                                          | Choices     | Required |
|-------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------|----------|
| docker_registry         | Container registry URL                                                             | "{{ lookup('env', 'DOCKER_REGISTRY') or 'docker.io' }}"          | string      | no       |
| docker_username         | Username for container registry                                                    | "{{ lookup('env', 'DOCKER_USERNAME') }}"                         | string      | yes      |
| docker_password         | Password for container registry                                                    |  "{{ lookup('env', 'DOCKER_PASSWORD') }}"                        | string      | yes      |
| web_app_name            | Name of a web application                                                          | "web_app"                                                        | string      | no       |
| web_app_deploy_dir      | Docker-compose deployment  target directory                                        | "/home/{{ ansible_user }}/services/{{ web_app_name }}"           | string      | no       |
| web_app_full_wipe       | Enforces clean installation via preliminary complete  delition of application data | false                                                            | true, false | no       |
| web_app_container_image | URL of the Docker image                                                            | "{{ docker_registry }}/{{ docker_username }}/{{ web_app_name }}" | string      | no       |
| web_app_port_host       | Forwarded port at host                                                             | 80                                                               | 0-65536     | no       |
| web_app_port_docker     | Forwarded port in container                                                        | 80                                                               | 0-65536     | no       |


---


Dependencies
===

- Roles
    - `docker` - custom role which performs clean installation of docker on the target host
- Collections
    - `community.docker`


Example Playbook
----------------

```yml
- hosts: webservers
  become: true
  roles:
    - "web_app"
  vars:
    web_app_name: app_python
    web_app_port_host: 3000
    web_app_port_docker: 8000
  vars_files:
    - ../../../host_vars/yacloud.yml
    - ../../../group_vars/all.yml
```