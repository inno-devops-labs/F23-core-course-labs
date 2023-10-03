# Docker Role

This Ansible role installs Docker and Docker Compose using pip.

## Requirements:
- Target machine(s) must have Python3 and APT (For Debian-based distributions).

## Usage:
Include this role in your playbooks:
```
roles:
  - docker
```

### 4. Deployment:
Run the playbook using (you must locate in `ansible` folder to apply `ansible.cfg`):

```
ansible-playbook playbooks/dev/main.yaml --diff
```