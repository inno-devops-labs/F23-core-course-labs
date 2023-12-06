Web app
=========

This role can deploy or destroy python_app.

Requirements
------------

Installed docker or docker role as a dependency

Role Variables
--------------

docker_app_name - name of the container
docker_compose_proj - name of directory in /opt where compose file will be located
docker_port - external port for the container
docker_image - name of the image from docker registry

Dependencies
------------

docker role

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: web_app, docker_app_name: "app", docker_compose_proj: "compose_app_dir", docker_port: 8080, docker_image: "app:latest" }

License
-------

BSD
