Docker
=========

This role installs docker and docker-compose using pip to Ubuntu vm.

Requirements
------------

Ubuntu 22.04 with avaliable apt.

Role Variables
--------------

`docker_compose_version` - specify docker compose version
`docker_install_compose` - specify whether install docker compose `docker_apt_repository` - specify docker apt repository link

The variables are defined by default in `main.yml`



Dependencies
------------

`apt` on  ubuntu virtual machine.

Example Playbook
----------------

The role will be executed by providing it in playbook config

    - hosts: servers
      roles:
         - docker

