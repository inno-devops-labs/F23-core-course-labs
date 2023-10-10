Web App
=========

Web App role for Ansible, to install Docker and deploy Moscow time application on remote server


Requirements
------------

It is strongly recommended to utilize Ubuntu 22.04 LTS as the preferred Linux distribution version, as the `web_app` role has been thoroughly tested on this particular release.

Role Variables
--------------

| Variable              | Required | Default                         | Choices                              | Comments                                                     |
| --------------------- | -------- | ------------------------------- | ------------------------------------ | ------------------------------------------------------------ |
| web_app_full_wipe     | yes      | no                              | no, yes                              | enables cleaning docker and app related files on remote server |
| app_folder_path       | yes      | home/{{ ansible_ssh_user }}/app | any suitable path                    | path, where application files will be stored                 |
| docker_image_name     | yes      | time_app:latest                 | any docker acceptable image name     | docker image name that will be build on remote server        |
| docker_container_name | yes      | time_app                        | any docker acceptable container name | docker container name that will be build on remote server    |
| docker_ports          | yes      | 80:5000                         | ANY:5000                             | on which ports docker container will be ran                  |

Dependencies
------------

This role has dependency from another `docker` role. See **/roles/docker/README.md**  for more details

Example Playbook
----------------

    - name: Docker Installation
      hosts: yandex_cloud_01
      become: yes
      roles:
        - web_app

License
-------

```
MIT License

Copyright (c) 2023 Azamat Shakirov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



Author Information
------------------

Shakirov Azamat B20-CS

a.shakirov@innopolis.university