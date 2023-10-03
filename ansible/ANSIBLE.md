# Ansible Best Practices


I applied various best practices while implementing the lab that are listed [here](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html).

## Keep Simple
The project did not require having any complex features of Ansible. This enhances 
readability of the code.

## Naming
I named all playbooks and tasks properly to make the workflow readable.

## Comments
I also provided comments where necessary to make code understandable.

## Dynamic Inventory
I used dynamic inventory using `terraform-inventory` to enhance automation capabilities.

## Separation
All project files are split logically.


# Docker Role

I created a custom role for deployment.

## Checking Ansible Setup

```
$ ansible virtualmachines -m ping

vm01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

## Output

```
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Deploy Docker with Ansible role] ******************************************************

TASK [Gathering Facts] **********************************************************************
ok: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Files/Innopolis/Classes/4 year/1 Semester/DevOps/devops-course-labs/ansible/roles/docker/tasks/install_pip.yml for vm01

TASK [docker : Update apt] ******************************************************************
changed: [vm01]

TASK [docker : Install python and pip] ******************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 214 not upgraded.
changed: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Files/Innopolis/Classes/4 year/1 Semester/DevOps/devops-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm01

TASK [docker : Install docker] **************************************************************
changed: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Files/Innopolis/Classes/4 year/1 Semester/DevOps/devops-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm01

TASK [docker : Install docker-compose] ******************************************************
changed: [vm01]

PLAY RECAP **********************************************************************************
vm01                       : ok=8    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details

```
$ ansible-inventory -i inventory/inventory.yaml --list

{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_host": "84.23.55.246"
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

# Dynamic Inventory

In order to implement a dynamic inventory for my project, I used [terraform-inventory](https://github.com/adammck/terraform-inventory).
This tool allows me to retrieve the VM configuration and use it for Ansible.

To use it I created a `dynamic_inventory.sh` bash script which accesses the _.tfstate_ file and passes it further. This file is based on the solution from [this discussion](https://github.com/adammck/terraform-inventory/issues/121).

Another possible way to use it is to cd to _terraform/vkcloud_ folder first:

`cd terraform/vkcloud`

And then, run the following command and provide the full path to _terraform-inventory_ executable:

`ansible-playbook --inventory-file="path to exe of terraform inventory" "../../playbooks/dev/main.yaml"`

The result of the execution is pretty the same as the one from output above.