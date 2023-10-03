# Ansible

## Ansible best practices:
* Configuration file ansible.cfg not to repeat useful information.
* Using roles instead of a huge list of tasks inside a playbook.
* Good naming of tasks.
* Using version control. Keeping your playbooks and inventory file in git.

## Task 1:
```
become-pass
BECOME password: 

PLAY [Playbook with existing Ansible role] *****************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/ilya/Документы/DevOps/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for localhost

TASK [docker : Install pip] ********************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/ilya/Документы/DevOps/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install docker] *****************************************************************************************
changed: [localhost]

TASK [docker : include_tasks] ******************************************************************************************
included: /home/ilya/Документы/DevOps/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Install Docker Compose] *********************************************************************************
changed: [localhost]

PLAY RECAP *************************************************************************************************************
localhost                  : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
## Task 2

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
## Inventory local:

```
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}
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


