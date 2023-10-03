

## Deployment

```

> ansible-playbook playbooks/dev/main.yml --diff 

PLAY [Deploy docker] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [vk_cloud]

TASK [docker : include_tasks] **************************************************
included: /home/bekzat/Documents/Innopolis/4_years/DevOps/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for vk_cloud

TASK [docker : Update apt] *****************************************************
changed: [vk_cloud]

TASK [docker : Install python and pip] *****************************************
ok: [vk_cloud]

TASK [docker : include_tasks] **************************************************
included: /home/bekzat/Documents/Innopolis/4_years/DevOps/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vk_cloud

TASK [docker : Install docker] *************************************************
ok: [vk_cloud]

TASK [docker : include_tasks] **************************************************
included: /home/bekzat/Documents/Innopolis/4_years/DevOps/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vk_cloud

TASK [docker : Install docker-compose] *****************************************
ok: [vk_cloud]

PLAY RECAP *********************************************************************
vk_cloud                   : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  

```

```
 > ansible-inventory -i inventory/default.yml --list{
    "_meta": {
        "hostvars": {
            "vk_cloud": {
                "ansible_host": "212.233.95.2"
            }
        }
    },
    "all": {
        "children": [
            "lab_hosts",
            "ungrouped"
        ]
    },
    "lab_hosts": {
        "hosts": [
            "vk_cloud"
        ]
    }
}

 ```