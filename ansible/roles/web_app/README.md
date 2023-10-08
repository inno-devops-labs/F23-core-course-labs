# Web Application

## Description

This role launches the web application in Docker container and exposes ports.
If Docker is not installed then run this role with tag `docker`, it will install the Docker with Docker compose.

The user can define an application to run, its Docker image, container name, and what port to expose.

Also, the role has ability to wipe the logic. So, user can stop and remove the container of the application.

### Modes

The role can work in 2 modes: 
- **container mode**: launch the application in Docker container. Tag: `web_app_run_container`
- **docker compose mode** (default): launch the application using Docker Compose file.
Template for this mode you can find in `templates` folder. Tag: `web_app_run`

## Wipe the application

To stop and remove container you should use tag `web_app_wipe` (docker compose mode) or `web_app_wipe_container`
(container mode) within running a playbook, and set variable `web_app_full_wipe: true`:
```shell
ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/app_python/main.yaml --tags web_app_wipe
```

Output:
```text
...

TASK [web_app : include_tasks] **************************************************************************************
included: .../ansible/roles/web_app/tasks/0-wipe.yml for my-vm-2, my-vm-1

TASK [web_app : Stop and Delete the container] **********************************************************************
changed: [my-vm-2]
changed: [my-vm-1]

PLAY RECAP **********************************************************************************************************
my-vm-1                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
my-vm-2                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```