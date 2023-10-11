## Lab 5

- ansible-playbook ./playbooks/dev/main.yaml --diff

```
PLAY [Deploy Docker] ***************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [vm]

TASK [docker : Install pip] ********************************************************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for vm

TASK [docker : Update apt] *********************************************************************************************************************
changed: [vm]

TASK [docker : Install Python] *****************************************************************************************************************
ok: [vm]

TASK [docker : Install pip] ********************************************************************************************************************
ok: [vm]

TASK [docker : Install Docker] *****************************************************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : Install Docker] *****************************************************************************************************************
ok: [vm]

TASK [docker : Install Docker Compose] *********************************************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : Install Docker Compose] *********************************************************************************************************
ok: [vm]

PLAY RECAP *************************************************************************************************************************************
vm                         : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

- ansible-inventory -i inventory/default_ya.yml --list

```
{
    "_meta": {
        "hostvars": {
            "vm": {
                "ansible_become": true,
                "ansible_host": "62.84.121.53",
                "ansible_ssh_private_key_file": "~/.ssh/id_test",
                "ansible_user": "wareverdud"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex-cloud"
        ]
    },
    "yandex-cloud": {
        "hosts": [
            "vm"
        ]
    }
}
```

## Lab 6

- ansible-playbook ./playbooks/dev/main.yaml

```
PLAY [Deploy App] ***********************************************************************************************

TASK [Gathering Facts] ******************************************************************************************
ok: [vm]

TASK [docker : Check old versions of Docker are not installed] **************************************************
ok: [vm]

TASK [docker : Check dependencies are installed] ****************************************************************
ok: [vm]

TASK [docker : Check additional dependencies are installed] *****************************************************
ok: [vm]

TASK [docker : Check curl is present] ***************************************************************************
ok: [vm]

TASK [docker : include_tasks] ***********************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : Add Docker apt key] ******************************************************************************
ok: [vm]

TASK [docker : Add Docker apt key] ******************************************************************************
skipping: [vm]

TASK [docker : Add Docker repository] ***************************************************************************
ok: [vm]

TASK [docker : Install Docker packages] *************************************************************************
skipping: [vm]

TASK [docker : Install Docker packages] *************************************************************************
ok: [vm]

TASK [docker : Check Docker is started and enabled at boot] *****************************************************
ok: [vm]

TASK [docker : Check handlers are notified now to avoid firewall conflicts] *************************************

TASK [docker : include_tasks] ***********************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : Check Docker Compose version] ********************************************************************
ok: [vm]

TASK [docker : set_fact] ****************************************************************************************
ok: [vm]

TASK [docker : Delete existing Docker Compose version] **********************************************************
skipping: [vm]

TASK [docker : Install Docker Compose] **************************************************************************
skipping: [vm]

TASK [docker : include_tasks] ***********************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/docker/tasks/install_docker_python.yml for vm

TASK [docker : Install required system packages] ****************************************************************
ok: [vm]

TASK [docker : Install Docker for Python] ***********************************************************************
ok: [vm]

TASK [docker : Install Docker Compose module for Python] ********************************************************
ok: [vm]

TASK [docker : Get docker group info using getent] **************************************************************
ok: [vm]

TASK [docker : Ensure docker users are added to the docker group] ***********************************************
ok: [vm] => (item=wareverdud)

TASK [docker : Reset ssh connection to apply user changes] ******************************************************

TASK [web_app : Create Docker Compose file] *********************************************************************
ok: [vm]

TASK [web_app : Create and Start the container] *****************************************************************
ok: [vm]

TASK [web_app : Show results] ***********************************************************************************
ok: [vm] => {
    "output": {
        "actions": [],
        "changed": false,
        "failed": false,
        "services": {
            "app_python": {
                "app_python": {
                    "cmd": [],
                    "image": "wareverdud/lab3:latest",
                    "labels": {
                        "com.docker.compose.config-hash": "56eec34976be2ba5f9f9aead98aed48382dcd0fa10a3394a1613601ceba51ff3",
                        "com.docker.compose.container-number": "1",
                        "com.docker.compose.oneoff": "False",
                        "com.docker.compose.project": "wareverdud",
                        "com.docker.compose.project.config_files": "docker-compose.yml",
                        "com.docker.compose.project.working_dir": "/home/wareverdud",
                        "com.docker.compose.service": "app_python",
                        "com.docker.compose.version": "1.29.0"
                    },
                    "networks": {
                        "wareverdud_default": {
                            "IPAddress": "172.18.0.2",
                            "IPPrefixLen": 16,
                            "aliases": [
                                "66b70ba572b2",
                                "app_python"
                            ],
                            "globalIPv6": "",
                            "globalIPv6PrefixLen": 0,
                            "links": null,
                            "macAddress": "02:42:ac:12:00:02"
                        }
                    },
                    "state": {
                        "running": true,
                        "status": "running"
                    }
                }
            }
        }
    }
}

TASK [web_app : Verify app is running] **************************************************************************
ok: [vm] => {
    "changed": false,
    "msg": "All assertions passed"
}

TASK [web_app : include_tasks] **********************************************************************************
included: /home/wareverdud/Desktop/core-course-labs/ansible/roles/web_app/tasks/wipe.yml for vm

TASK [web_app : Tear down existing services] ********************************************************************
skipping: [vm]

PLAY RECAP ******************************************************************************************************
vm                         : ok=24   changed=0    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
```