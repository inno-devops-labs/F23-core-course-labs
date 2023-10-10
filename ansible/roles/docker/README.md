Docker
=========

Ansible role which installs Docker using on the host 

Role Variables
--------------

| Variable                | Required | Default | Choices                   | 
|-------------------------|----------|---------|---------------------------|
| docker_install_compose  | no       | true    | true, false               | 

- Specifies whether `docker-compose` should be installed amongside docker 


Example Playbook
----------------

```yml
- hosts: all
  become: true
  roles:
    - docker
```