## Docker Role Deployment:

```
ansible-playbook playbooks/dev/main.yaml --diff

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [vm1]

TASK [docker : include_tasks] **************************************************
included: /Users/aisen/Desktop/devOpsCourse/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm1

TASK [docker : Install pip] ****************************************************
ok: [vm1]

TASK [docker : Install Docker using pip] ***************************************
ok: [vm1]

TASK [docker : include_tasks] **************************************************
included: /Users/aisen/Desktop/devOpsCourse/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm1

TASK [docker : Install Docker Compose using pip] *******************************
ok: [vm1]

PLAY RECAP *********************************************************************
vm1                        : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Inventory Details:

```
ansible-inventory -i inventory/myhosts.yml --list 

{
    "_meta": {
        "hostvars": {
            "vm1": {
                "ansible_host": "192.168.64.2",
                "ansible_python_interpreter": "/usr/bin/python3",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "aisen"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "vm1"
        ]
    }
}
```