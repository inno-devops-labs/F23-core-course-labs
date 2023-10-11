# Ansible and Docker Deployment 
> Deploying Docker on a newly created cloud VM with Ansible.

## Part 1: Initial Setup 

1. Repository Structure & Installation : 
    - I organized my repository following the recommended structure.
    - Ansible was successfuly installed.

2. Ansible Role and Playbook : 
    - I used a recommended ansible role, that I downloaded from `ansible-galaxy` - [geerling.docker](https://github.com/geerlingguy/ansible-role-docker)
    - Created a playbook that I used in order to deploy Docker on a server 

## Part 2: Custom Docker Role 

3. Deployement Output :
> Last 50 lines of the ouputs form the deployement command, obtained using `ansible-playbook <path_to your_playbook> --diff` command.

```sh
TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ****************************************************

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************
skipping: [server]

TASK [geerlingguy.docker : Get docker group info using getent.] ******************************************************************************
skipping: [server]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *********************************************************
skipping: [server]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************
skipping: [server]

PLAY [Deploying custom Docker role] **********************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************
ok: [server]

TASK [docker : include_tasks] ****************************************************************************************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for server

TASK [docker : Install pip] ******************************************************************************************************************
ok: [server]

TASK [docker : include_tasks] ****************************************************************************************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for server

TASK [docker : Add Docker GPG apt Key] *******************************************************************************************************
ok: [server]

TASK [docker : Add Docker Repository] ********************************************************************************************************
ok: [server]

TASK [docker : Update apt and install docker-ce] *********************************************************************************************
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following packages will be upgraded:
  docker-ce
1 upgraded, 0 newly installed, 0 to remove and 19 not upgraded.
changed: [server]

TASK [docker : include_tasks] ****************************************************************************************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for server

TASK [docker : Install Docker Compose using pip] *********************************************************************************************
ok: [server]

PLAY RECAP ***********************************************************************************************************************************
server                     : ok=22   changed=4    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
```

4. Inventory Details : 

> Inventory Details ouput obtained using `ansible-inventory -i inventory/default-ya-cloud.yaml --list`

```sh
{
    "_meta": {
        "hostvars": {
            "server": {
                "ansible_host": "158.160.102.54",
                "ansible_ssh_private_key_file": "/Users/m4k4rich/.ssh/id_ed25519",
                "ansible_user": "mainuser"
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

5. Best Practices : 
    - Modules are responsible for one simple & small task.
    - Every task has a meaningful name, empty lines are used for readability 
    - Usage of recommended directory structure. 
    - Application of `ansible-playbook --check`, in order to check on actions before taking them. 
    - Usage of dynamic inventory ( from bonus task ) that allows to avoid manual host configuration.    

## Part 3: Deploying Python Application 

```sh
ok: [server]

TASK [docker : Add Docker Repository] ******************************************
ok: [server]

TASK [docker : Update apt and install docker-ce] *******************************
ok: [server]

TASK [docker : include_tasks] **************************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for server

TASK [docker : Install Docker Compose using pip] *******************************
ok: [server]

TASK [web_app : Wiping containers] *********************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for server

TASK [web_app : Check for the existance of /python_app] ************************
ok: [server]

TASK [web_app : Check for the existance of Docker Compose File] ****************
ok: [server]

TASK [web_app : Removing existing Docker Compose containers] *******************
changed: [server]

TASK [web_app : Removing existing Docker Compose files] ************************
changed: [server]

TASK [web_app : Remove app directory /python_app] ******************************
ok: [server]

TASK [web_app : Create directory for the python_app container] *****************
ok: [server]

TASK [web_app : Copy Docker Compose] *******************************************
changed: [server]

TASK [web_app : Run Docker Compose] ********************************************
changed: [server]

TASK [Check if the service is healthy] *****************************************
ok: [server]

TASK [Handle the health check result] ******************************************
skipping: [server]

PLAY RECAP *********************************************************************
server                     : ok=20   changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
```

## Part 3: Deploying Node Application 

```sh
ok: [server]

TASK [docker : Add Docker Repository] ******************************************
ok: [server]

TASK [docker : Update apt and install docker-ce] *******************************
ok: [server]

TASK [docker : include_tasks] **************************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for server

TASK [docker : Install Docker Compose using pip] *******************************
ok: [server]

TASK [web_app : Wiping containers] *********************************************
included: /Users/m4k4rich/core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for server

TASK [web_app : Check for the existance of /my-random-node-app] ****************
ok: [server]

TASK [web_app : Check for the existance of Docker Compose File] ****************
ok: [server]

TASK [web_app : Removing existing Docker Compose containers] *******************
skipping: [server]

TASK [web_app : Removing existing Docker Compose files] ************************
skipping: [server]

TASK [web_app : Remove app directory /my-random-node-app] **********************
ok: [server]

TASK [web_app : Create directory for the my-random-node-app container] *********
ok: [server]

TASK [web_app : Copy Docker Compose] *******************************************
changed: [server]

TASK [web_app : Run Docker Compose] ********************************************
changed: [server]

TASK [Check if the service is healthy] *****************************************
ok: [server]

TASK [Handle the health check result] ******************************************
skipping: [server]

PLAY RECAP *********************************************************************
server                     : ok=18   changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0   

```