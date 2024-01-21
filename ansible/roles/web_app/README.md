Docker Role
=========

The web_app role is used to deploy the app_python on VM,
using Docker image.

Requirements
------------

In case, if the Docker is not installed on the target machine,
it will use previously created "docker" role

Role Variables
--------------

Additional "docker" role

Example Playbook
----------------

    - hosts: vms
      roles:
         - { role: username.rolename }

