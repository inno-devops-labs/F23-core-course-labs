
To utilize docker role it is enough to mention it in the playbook file as:
```yaml
roles:
    - { role: docker, become: yes }
```

Note: make sure your `ansible.cfg` contains correct `role_path` specification.

For example, it could be `roles_path=:/roles` if the ansible-playbook runs from `ansible/` directory 