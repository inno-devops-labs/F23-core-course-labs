Docker
=========

Docker role for Ansible to install Docker and Docker-compose via pip




Requirements
------------

It is strongly recommended to utilize Ubuntu 22.04 LTS as the preferred Linux distribution version, as the docker role has been thoroughly tested on this particular release.

Role Variables
--------------

No role variables

Dependencies
------------

No dependencies

Example Playbook
----------------

    - name: Docker Installation
      hosts: yandex_cloud_01
      become: yes
      roles:
        - docker

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