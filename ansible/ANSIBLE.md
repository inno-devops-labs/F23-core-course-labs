# Ansible

## Best practices
* Names for plays and tasks
* Using YAML syntax
* Following the recommended structure if files and directories
* Have the secure storage for secrets

## Docker role

**_Note: run from `ansible` directory_**

Output for `ansible-playbook --ask-become-pass playbooks/dev/main.yml` command

<details>

```
BECOME password: 

PLAY [playbook] ************************************************************************************************************************************************************

TASK [docker : Install pip] ************************************************************************************************************************************************
ok: [vm]

TASK [docker : Include install_docker] *************************************************************************************************************************************
included: /ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : Install docker] *********************************************************************************************************************************************
ok: [vm]

TASK [docker : Include install_compose] ************************************************************************************************************************************
included: /ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : install docker-compose] *************************************************************************************************************************************
ok: [vm]

PLAY RECAP *****************************************************************************************************************************************************************
vm                         : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
</details>

Output for `ansible-inventory -i inventory/default_aws_ec2.yml --list` command
<details>

```
{
    "_meta": {
        "hostvars": {
            "vm": {
                "ansible_host": "203.0.113.111",
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
            "vm"
        ]
    }
}
```

</details>

## Dynamic Inventory

For this task I used Yandex Cloud. 
> I know that last time I used VK Cloud, however I faced
some issues with my account and still don't have access to it.
Until I resolve the issue I'll use Yandex Cloud.

Output for `ansible-playbook --ask-become-pass playbooks/dev/main.yml` command

<details>

```
BECOME password: 

PLAY [playbook] ************************************************************************************************************************************************************

TASK [docker : Install pip] ************************************************************************************************************************************************
ok: [server]

TASK [docker : Include install_docker] *************************************************************************************************************************************
included: /ansible/roles/docker/tasks/install_docker.yml for server

TASK [docker : Install docker] *********************************************************************************************************************************************
ok: [server]

TASK [docker : Include install_compose] ************************************************************************************************************************************
included: /ansible/roles/docker/tasks/install_compose.yml for server

TASK [docker : install docker-compose] *************************************************************************************************************************************
ok: [server]

PLAY RECAP *****************************************************************************************************************************************************************
server                     : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
</details>

Output for ` ansible-inventory -i inventory/default_yacloud.yml --list` command

<details>

```
{
    "_meta": {
        "hostvars": {
            "server": {
                "ansible_host": "84.201.175.92",
                "ansible_ssh_private_key_file": "/path-to-your-private-key",
                "ansible_user": "liza"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "web_servers"
        ]
    },
    "web_servers": {
        "hosts": [
            "server"
        ]
    }
}

```

</details>
