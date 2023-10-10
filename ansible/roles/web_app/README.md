# Web App Ansible Role

This Ansible role is designed to deploy and manage a web application on target servers. It includes tasks to install necessary dependencies, start the web application using Docker, and perform a wipe operation to remove the application and its related resources.

## Role Dependencies

This role depends on the following roles:

- `docker`: This role is used for managing Docker containers. Ensure that the `docker` role is available in your Ansible roles path.

## Role Variables

This role uses the following variables:

- `web_app_full_wipe` (default: `false`): Set this variable to `true` to enable a full wipe of the application, which includes stopping Docker containers and removing related files. By default, it is set to `false`.

## Tasks

The role contains the following tasks:

1. **Check Dependencies (`check_deps`)**
   - Ensures that Docker is installed on the target servers.

2. **Wipe (`wipes`)**
   - Includes tasks from `roles/web_app/tasks/0-wipe.yml` only if `web_app_full_wipe` is set to `true`. These tasks stop Docker containers and remove related resources.

3. **Start Application (`run_docker`)**
   - Uses the `docker_container` module to start the web application in a Docker container. It exposes port 80 on the host.

## Example Playbook Usage

Here's an example of how to use this role in your Ansible playbook:

```yaml
---
- name: Deploy and Manage Web App
  hosts: web_servers
  become: true
  roles:
    - web_app
```

## How to Enable Full Wipe

To enable a full wipe of the application, set the `web_app_full_wipe` variable to `true` when running your playbook:

```bash
ansible-playbook your_playbook.yml -e "web_app_full_wipe=true"
```

This will execute the wipe tasks in addition to the deployment tasks, stopping Docker containers and removing related resources.