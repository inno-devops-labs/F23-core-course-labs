# Ansible

## Docker role
The docker role and its README can be found inside `roles/docker`

## Docker playbook
The docker playbook is `docker.yml`

## Inventory
The inventory should be created manually and is omitted from this repository for safety reasons

## Best practices
https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html

I was following the best practices from the link above to a reasonable extent

## Deplyoment logs
```
ok: [<ip-address>]

TASK [docker : include_tasks] **************************************************
included: /home/adachi/core-course-labs/ansible/roles/docker/tasks/deps.yaml for <ip-address>

TASK [docker : Ensure dependencies are installed.] *****************************
ok: [<ip-address>]

TASK [docker : include_tasks] **************************************************
included: /home/adachi/core-course-labs/ansible/roles/docker/tasks/repo.yaml for <ip-address>

TASK [docker : Install keys] ***************************************************
ok: [<ip-address>]

TASK [docker : Add docker repo] ************************************************
ok: [<ip-address>]

TASK [docker : include_tasks] **************************************************
included: /home/adachi/core-course-labs/ansible/roles/docker/tasks/install.yaml for <ip-address>

TASK [docker : Ensure unnecessary, unofficial or old packages are removed] *****
ok: [<ip-address>]

TASK [docker : Install docker] *************************************************
ok: [<ip-address>]

TASK [docker : Install pip packets] ********************************************
ok: [<ip-address>]

TASK [web_app : Install application] *******************************************
included: /home/adachi/core-course-labs/ansible/roles/web_app/tasks/run.yaml for <ip-address>

TASK [web_app : Create a directory if it does not exist] ***********************
changed: [<ip-address>]

TASK [web_app : Create docker-compose] *****************************************
changed: [<ip-address>]

TASK [web_app : Run application] ***********************************************
changed: [<ip-address>]

TASK [web_app : Wipe appliction] ***********************************************
skipping: [<ip-address>]

PLAY RECAP *********************************************************************
<ip-address>             : ok=28   changed=6    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   


EXIT NOTICE [Playbook execution success] **************************************
===============================================================================
```
