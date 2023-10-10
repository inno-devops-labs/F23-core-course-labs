# Playbook usage example

```
- name: Dev
  gather_facts: no
  hosts: localhost
  connection: local
  become: true
  roles:
    - ansible/roles/docker
```

# Requirements 

* python3-pip
