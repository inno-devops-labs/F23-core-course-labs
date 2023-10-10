# Output
```
╰─➤  ansible-playbook -i inventory main.yml --diff
...

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************************
included: /home/bizuki/proj/devops-course/ansible/roles/docker/tasks/clean.yml for main

TASK [docker : Remove old packages] **********************************************************************************************************************************************************************************
ok: [main]

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************************
included: /home/bizuki/proj/devops-course/ansible/roles/docker/tasks/docker_apt.yml for main

TASK [docker : Install dependencies] *********************************************************************************************************************************************************************************
ok: [main]

TASK [docker : Add Docker apt key.] **********************************************************************************************************************************************************************************
ok: [main]

TASK [docker : get arch] *********************************************************************************************************************************************************************************************
changed: [main]

TASK [docker : gat release] ******************************************************************************************************************************************************************************************
changed: [main]

TASK [docker : Add docker repo.] *************************************************************************************************************************************************************************************
ok: [main]

TASK [docker : Update package list] **********************************************************************************************************************************************************************************
ok: [main]

TASK [docker : include_tasks] ****************************************************************************************************************************************************************************************
included: /home/bizuki/proj/devops-course/ansible/roles/docker/tasks/install_docker.yml for main

TASK [docker : install docker] ***************************************************************************************************************************************************************************************
ok: [main]

TASK [web_app : include_tasks] ***************************************************************************************************************************************************************************************
included: /home/bizuki/proj/devops-course/ansible/roles/web_app/tasks/check_deps.yml for main

TASK [web_app : check and install deps] ******************************************************************************************************************************************************************************
ok: [main]

TASK [web_app : include_tasks] ***************************************************************************************************************************************************************************************
included: /home/bizuki/proj/devops-course/ansible/roles/web_app/tasks/run.yml for main

TASK [web_app : Create app] ******************************************************************************************************************************************************************************************
[DEPRECATION WARNING]: The container_default_behavior option will change its default value from "compatibility" to "no_defaults" in community.docker 2.0.0. To remove this warning, please specify an explicit value 
for it now. This feature will be removed from community.docker in version 2.0.0. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
ok: [main]

PLAY RECAP ***********************************************************************************************************************************************************************************************************
main                       : ok=16   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

# Inventory
I used static inventory (no bonus) and just specifed previously created vm in lab4. The interesting thing is ubuntu on that machine is going with python preinstalled but it has old version thus I redefined interpreter in config for this host.

```
╭─bizuki@DESKTOP-A1F8O7S ~/proj/devops-course/ansible  ‹lab5*› 
╰─➤  ansible-inventory -i inventory/yandex.yml --list 
{
    "_meta": {
        "hostvars": {
            "main": {
                "ansible_host": "158.160.122.93",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex"
        ]
    },
    "yandex": {
        "hosts": [
            "main"
        ]
    }
}
```
