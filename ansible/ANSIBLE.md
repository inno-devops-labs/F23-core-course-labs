# Ansible

## Ansible best practices:
* Configuration file ansible.cfg not to repeat useful information.
* Using roles instead of a huge list of tasks inside a playbook.
* Good naming of tasks.
* Using version control. Keeping your playbooks and inventory file in git.

```
PLAY [Deploy Docker] ************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************
ok: [lab5_vm]

TASK [docker : Install pip] *****************************************************************************************************************************
included: {...}/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for lab5_vm

TASK [docker : Update apt] ******************************************************************************************************************************
changed: [lab5_vm]

TASK [docker : Install python] **************************************************************************************************************************
ok: [lab5_vm]

TASK [docker : Install pip] *****************************************************************************************************************************
changed: [lab5_vm]

TASK [docker : Install docker] **************************************************************************************************************************
included: {...}/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_lab5_vm

TASK [docker : Install docker] **************************************************************************************************************************
changed: [lab5_vm]

TASK [docker : Install docker-compose] ******************************************************************************************************************
included: {...}/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for lab5_vm

TASK [docker : Install docker-compose via pip] **********************************************************************************************************
changed: [lab5_vm]

PLAY RECAP **********************************************************************************************************************************************
lab5_vm            : ok=9    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory
```
{
    "_meta": {
        "hostvars": {
            "lab5_vm": {
                "ansible_host": "84.160.162.199",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_b_vms"
        ]
    },
    "yandex_b_vms": {
        "hosts": [
            "lab5_vm"
        ]
    }
}
```

# Deployment:

## app_python:

```
TASK [docker : Install python3-pip via apt] ************************************
ok: [terraform-vm]

TASK [docker : Install docker-compose using pip] *******************************
included: {...}/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for lab6-vm

TASK [docker : Install docker-compose via pip] *********************************
ok: [lab6-vm]

TASK [web_app : Check web_app_deployment_way] **********************************
skipping: [lab6-vm]

TASK [web_app : Get container info] ********************************************
ok: [lab6-vm]

TASK [web_app : Stop container if it is running] *******************************
skipping: [lab6-vm]

TASK [web_app : Check Docker-Compose file exists] ******************************
skipping: [lab6-vm]

TASK [web_app : Stop Docker-Compose services] **********************************
skipping: [lab6-vm]

TASK [web_app : Remove container] **********************************************
ok: [lab6-vm]

TASK [web_app : Remove image] **************************************************
ok: [lab6-vm]

TASK [web_app : Check Docker-Compose file exists] ******************************
skipping: [lab6-vm]

TASK [web_app : Remove Docker-Compose services] ********************************
skipping: [lab6-vm]

TASK [web_app : Remove application's directory with it's content] **************
skipping: [lab6-vm]

TASK [web_app : Deploy Application using Docker] *******************************
changed: [lab6-vm]

TASK [web_app : Create application directory] **********************************
skipping: [lab6-vm]

TASK [web_app : Create Docker-Compose file from template] **********************
skipping: [lab6-vm]

PLAY RECAP *********************************************************************
lab6-vm               : ok=18   changed=1    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
```

## app_go:

```
TASK [docker : Install python3-pip via apt] ************************************
ok: [terraform-vm]

TASK [docker : Install docker-compose using pip] *******************************
included: {...}/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for lab6-vm

TASK [docker : Install docker-compose via pip] *********************************
ok: [lab6-vm]

TASK [web_app : Check web_app_deployment_way] **********************************
skipping: [lab6-vm]

TASK [web_app : Get container info] ********************************************
ok: [lab6-vm]

TASK [web_app : Stop container if it is running] *******************************
skipping: [lab6-vm]

TASK [web_app : Check Docker-Compose file exists] ******************************
skipping: [lab6-vm]

TASK [web_app : Stop Docker-Compose services] **********************************
skipping: [lab6-vm]

TASK [web_app : Remove container] **********************************************
ok: [lab6-vm]

TASK [web_app : Remove image] **************************************************
ok: [lab6-vm]

TASK [web_app : Check Docker-Compose file exists] ******************************
skipping: [lab6-vm]

TASK [web_app : Remove Docker-Compose services] ********************************
skipping: [lab6-vm]

TASK [web_app : Remove application's directory with it's content] **************
skipping: [lab6-vm]

TASK [web_app : Deploy Application using Docker] *******************************
changed: [lab6-vm]

TASK [web_app : Create application directory] **********************************
skipping: [lab6-vm]

TASK [web_app : Create Docker-Compose file from template] **********************
skipping: [lab6-vm]

PLAY RECAP *********************************************************************
lab6-vm               : ok=18   changed=1    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
```

