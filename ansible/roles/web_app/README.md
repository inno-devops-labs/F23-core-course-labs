# web_app role
Role to deploy web app.

## Requirements
no

## Dependencies
docker role

## Example Playbook
```yml
- name: Deploy Python app
  hosts: all
  become: true
  roles:
    - role: web_app
      image: seakysneka1/webserv_python
      ports:
        - "8000:8000"
```

## Author Information
Sergei Pasynkov