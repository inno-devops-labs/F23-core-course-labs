# Ansible

## Best Practices

1. Deployment-specific custom role.

2. Task division between separate files.

3. 'terraform-inventory' dynamic inventory was utilized.

4. Simple structure of Ansible part. 
   Common ansible features, appropriate file names and etc. makes the code easier to read.

## Ansible Output

```
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Docker deployment using the Ansible role] ******************************************************

TASK [Gathering Facts] **********************************************************************
ok: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Users/Владимир/Desktop/Inno/devops/devops-course-labs/ansible/roles/docker/tasks/pip_task.yml for vm01

TASK [docker : Update cache] ******************************************************************
changed: [vm01]

TASK [docker : Python3 and python3-pip installation] ******************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 214 not upgraded.
changed: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Users/Владимир/Desktop/Inno/devops/devops-course-labs/ansible/roles/docker/tasks/docker_task.yml for vm01

TASK [docker : Docker installation] **************************************************************
changed: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Users/Владимир/Desktop/Inno/devops/devops-course-labs/ansible/roles/docker/tasks/compose_task.yml for vm01

TASK [docker : Docker-compose installation] ******************************************************
changed: [vm01]

PLAY RECAP **********************************************************************************
vm01                       : ok=8    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

## Inventory Output

```
$ ansible-inventory -i inventory/inventory.yaml --list

{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_host": "212.233.94.135"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtualmachines"
        ]
    },
    "virtualmachines": {
        "hosts": [
            "vm01"
        ]
    }
}

```

## Dynamic Inventory Details
'inventory_dynamic.sh' bash script was created to represent dynamic inventory fucntionality.
This tool was used to obtain the virtual machine info and apply it to Ansible.
