## Deployment

```shell
  ansible-playbook playbooks/dev/main.yml --diff 
```

```text
PLAY [Deploy docker] ***********************************************************
TASK [Gathering Facts] *********************************************************
ok: [vk_cloud]
TASK [docker : include_tasks] **************************************************
included: D:/1_USER/Desktop/Arlan/Codes/Codes_Uni/4_year/DevOps/DevOps-course-labs/ansible/roles/docker/tasks/install_pip.yml for vk_cloud
TASK [docker : Update apt] *****************************************************
changed: [vk_cloud]
TASK [docker : Install python and pip] *****************************************
ok: [vk_cloud]
TASK [docker : include_tasks] **************************************************
included: D:/1_USER/Desktop/Arlan/Codes/Codes_Uni/4_year/DevOps/DevOps-course-labs/ansible/roles/docker/tasks/install_docker.yml for vk_cloud
TASK [docker : Install docker] *************************************************
ok: [vk_cloud]
TASK [docker : include_tasks] **************************************************
included: D:/1_USER/Desktop/Arlan/Codes/Codes_Uni/4_year/DevOps/DevOps-course-labs/ansible/roles/docker/tasks/install_compose.yml for vk_cloud
TASK [docker : Install docker-compose] *****************************************
ok: [vk_cloud]
PLAY RECAP *********************************************************************
vk_cloud                   : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

```text
 > ansible-inventory -i inventory/inventory.yml --list{
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