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