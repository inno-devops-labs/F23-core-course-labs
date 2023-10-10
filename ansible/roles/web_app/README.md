# Playbook usage example

```
- name: Dev
  gather_facts: no
  hosts: localhost
  connection: local
  become: true
  roles:
    - ansible/roles/web_app
```

# Requirements 

* docker
* docker-compose
