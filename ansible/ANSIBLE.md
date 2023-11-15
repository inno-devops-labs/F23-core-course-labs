### **Result of ansible-playbook playbooks/dev/main.yml --diff**

```
PLAY [Install docker] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************
ok: [vm]

TASK [docker : Update apt] ******************************************************************************************************************************************************************
changed: [vm]

TASK [docker : Install python and pip] ******************************************************************************************************************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 201 not upgraded.
changed: [vm]

TASK [docker : Install docker] **************************************************************************************************************************************************************
included: /home/ubuntu/devOps/devops-course-labs/ansible/roles/docker/tasks/docker.yml for vm

TASK [docker : Install docker] **************************************************************************************************************************************************************
ok: [vm]

TASK [docker : Install docker-compose] ******************************************************************************************************************************************************
included: /home/ubuntu/devOps/devops-course-labs/ansible/roles/docker/tasks/docker_compose.yml for vm

TASK [docker : Install docker-compose] ******************************************************************************************************************************************************
changed: [vm]

PLAY RECAP **********************************************************************************************************************************************************************************
vm                       : ok=9    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### **Inventory Details**

```
{
    "_meta": {
        "hostvars": {
            "vm":   {
                "ansible_host": "84.201.141.246"
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    }
    "virtual_machines": {
        "hosts": [
            "vm"
        ]
    }
}
```


