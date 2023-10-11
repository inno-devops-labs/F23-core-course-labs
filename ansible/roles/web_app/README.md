# web_app Ansible Role

This role deploys a web application using Docker.

## Requirements

- Docker installed on the target machine.
- Ansible `community.docker` collection.

## Role Variables

- `web_app_full_wipe`: When set to true, performs a full wipe of the application. Default is false.

## Usage

```
ansible-playbook -i inventory/myhosts.yml playbooks/dev/lab6.yaml -K
```

### To deploy only:

```
ansible-playbook -i inventory/myhosts.yml playbooks/dev/lab6.yaml --tags deploy -K
```

### To wipe:

```
ansible-playbook -i inventory/myhosts.yml playbooks/dev/lab6.yaml --tags wipe -K
```

## Dependencies

`docker` role

