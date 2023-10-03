# Ansible

## Docker role

### Command:
```
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --diff
```
### Output:
```
TASK [../../roles/docker : Ensure curl is present (on older systems without SNI).] ***
ok: [vm01]

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm01

TASK [../../roles/docker : Add Docker apt key.] ********************************
ok: [vm01]

TASK [../../roles/docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [vm01]

TASK [../../roles/docker : Add Docker repository.] *****************************
ok: [vm01]

TASK [../../roles/docker : Install Docker packages.] ***************************
skipping: [vm01]

TASK [../../roles/docker : Install Docker packages (with downgrade option).] ***
ok: [vm01]

TASK [../../roles/docker : Ensure Docker is started and enabled at boot.] ******
ok: [vm01]

TASK [../../roles/docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm01

TASK [../../roles/docker : Check current docker-compose version.] **************
ok: [vm01]

TASK [../../roles/docker : set_fact] *******************************************
ok: [vm01]

TASK [../../roles/docker : Delete existing docker-compose version if it's different.] ***
skipping: [vm01]

TASK [../../roles/docker : Install Docker Compose (if configured).] ************
skipping: [vm01]

TASK [../../roles/docker : Get docker group info using getent.] ****************
skipping: [vm01]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] ***
skipping: [vm01]

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ********

PLAY RECAP *********************************************************************
vm01                       : ok=13   changed=0    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0 
```
### Command:
```
ansible-inventory -i default_aws_ec2.yml --list 
```

### Output:

```
{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_host": "158.160.107.44",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "vm01"
        ]
    }
}
```

## Dynamic inventory 
I've used inventory plugin for Yandex Cloud proposed in the task.
###  Command:
```
ansible-playbook playbooks/dev/main.yaml --diff 
```
### Output:
```
TASK [../../roles/docker : Ensure curl is present (on older systems without SNI).] ***
ok: [terraform1]

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [../../roles/docker : Add Docker apt key.] ********************************
ok: [terraform1]

TASK [../../roles/docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [terraform1]

TASK [../../roles/docker : Add Docker repository.] *****************************
ok: [terraform1]

TASK [../../roles/docker : Install Docker packages.] ***************************
skipping: [terraform1]

TASK [../../roles/docker : Install Docker packages (with downgrade option).] ***
ok: [terraform1]

TASK [../../roles/docker : Ensure Docker is started and enabled at boot.] ******
ok: [terraform1]

TASK [../../roles/docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [../../roles/docker : Check current docker-compose version.] **************
ok: [terraform1]

TASK [../../roles/docker : set_fact] *******************************************
ok: [terraform1]

TASK [../../roles/docker : Delete existing docker-compose version if it's different.] ***
skipping: [terraform1]

TASK [../../roles/docker : Install Docker Compose (if configured).] ************
skipping: [terraform1]

TASK [../../roles/docker : Get docker group info using getent.] ****************
skipping: [terraform1]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] ***
skipping: [terraform1]

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ********

PLAY RECAP *********************************************************************
terraform1                 : ok=13   changed=0    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   
```

### Command:
```
ansible-inventory -i inventory/yacloud_compute.yml --list  
```

### Output:
```
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "158.160.107.44"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "terraform1"
        ]
    }
}

```

terraform1 - name of my VM in YandexCLoud, so dynamic host resolution works.