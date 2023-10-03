# Ansible Docker Role

This role installs docker, docker SDK and docker-compose.
Tested with Ubuntu 20.04, 22.04

## Requirements

None.

## Variables

See `defaults/main.yml` for full list of variables.

Modify `docker_ce_version` to choose the docker-ce version in apt.

Modify `compose_version` to modify docker compose version installed by pip.

## Dependencies

None.

## Example Playbook

```yaml
- name: Deploy Docker
    hosts: vms
    become: yes
    become_method: sudo
    roles:
    - docke
```
