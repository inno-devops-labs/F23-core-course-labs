# Web Application Deployment role

## Description and requirements
### Deps
- `docker` role
### Description
Role stands for continuous deployment of docker containers with docker-compose on a target machines. Role supports deploy, wiping and both options in order wipe -> deploy.
This provides an easy tool for management of docker containers on your machines.
## Usage
- Utilize this role by installing deps and adding it into your playbook, nothing in addition required
- Example of playbook usage:
```yml
- name: Test Playbook
  hosts: all
  roles:
    - name: web_app
      vars:
        app_name: test_app
        internal_port: 80
        external_port: 80
        buildroot: /test_app
```

- You can fully wipe without followed creation by:
    `ansible-playbook playbooks/dev/app_python/main.yml -e web_app_full_wipe=true --tags=" web_app_wipe"`