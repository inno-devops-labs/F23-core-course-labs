# Ansible

## Ansible best practices

* Using version control: Keeping your playbooks and inventory files in VSC like `git`
* Follow the directory structure: Organize your playbook directory structure (separating roles, host inventories, and group variables)
* Use dynamic inventory with clouds.
* Documentation: Document your playbooks, roles, and variables using comments or README files

## Deploy docker to web server

### Initial steps

* Generate ssh keys on host machine

```shell
ssh-keygen -t ed25519
```

* Connect to server and configure ssh to ansible user

```shell
sudo useradd -m -d /home/ansible-user -s /bin/bash ansible-user
sudo su - ansible-user
mkdir .ssh
touch .ssh/authorized_keys
echo "public_key" > /home/ansible-user/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

* Add password to ansible user (from root)

```shell
sudo passwd ansible-user
```

* Add ansible-uer to sudo group

```shell
sudo usermod -aG sudo ansible-user
```

### Check ansible connection

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible/inventory$ ansible web_server -m ping -i default_local.yml 
web_server | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

### Deploy docker

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible$ ansible-playbook -i inventory/default_local.yml playbooks/dev/main.yaml -K
BECOME password: 

PLAY [Deploy Docker] ******************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Ensure old versions of Docker are not installed.] **********************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Ensure dependencies are installed.] ************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ****************************************************************************************
skipping: [web_server]

TASK [../../roles/docker : Ensure curl is present (on older systems without SNI).] ****************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : include_tasks] *********************************************************************************************************************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/docker.yml for web_server

TASK [../../roles/docker : Add Docker apt key.] ***************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Add Docker apt key (alternative for older systems without SNI).] *******************************************************************************************
skipping: [web_server]

TASK [../../roles/docker : Add Docker repository.] ************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install Docker packages.] **********************************************************************************************************************************
skipping: [web_server]

TASK [../../roles/docker : Install Docker packages (with downgrade option).] **********************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Ensure Docker is started and enabled at boot.] *************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Ensure handlers are notified now to avoid firewall conflicts.] *********************************************************************************************

TASK [../../roles/docker : include_tasks] *********************************************************************************************************************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/docker-compose.yml for web_server

TASK [../../roles/docker : Check current docker-compose version.] *********************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : set_fact] **************************************************************************************************************************************************
skipping: [web_server]

TASK [../../roles/docker : Delete existing docker-compose version if it's different.] *************************************************************************************************
skipping: [web_server]

TASK [../../roles/docker : Install Docker Compose (if configured).] *******************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Get docker group info using getent.] ***********************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] ********************************************************************************************************
changed: [web_server] => (item=ansible-user)

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ***************************************************************************************************************

PLAY RECAP ****************************************************************************************************************************************************************************
web_server                 : ok=14   changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0   
```

### Inventory details

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible$ ansible-inventory -i inventory/default_local.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "xxx.xxx.xxx.xxx",
                "ansible_user": "ansible-user"
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
            "web_server"
        ]
    }
}
```

### Use pip for docker set up

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible$ ansible-playbook -i inventory/default_local.yml playbooks/dev/main.yaml -K
BECOME password: 

PLAY [Deploy Docker] ******************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install pip] ***********************************************************************************************************************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/pip.yml for web_server

TASK [../../roles/docker : Update apt] ************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install python] ********************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install pip] ***********************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install docker] ********************************************************************************************************************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/docker.yml for web_server

TASK [../../roles/docker : Install docker via pip] ************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Install docker-compose] ************************************************************************************************************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/docker-compose.yml for web_server

TASK [../../roles/docker : Install docker-compose via pip] ****************************************************************************************************************************
changed: [web_server]

PLAY RECAP ****************************************************************************************************************************************************************************
web_server                 : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

### Inventory details with docker via pip

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible$ ansible-inventory -i inventory/default_local.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "xxx.xxx.xxx.xxx",
                "ansible_user": "ansible-user"
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
            "web_server"
        ]
    }
}
```

## Dynamic inventory YandexCloud

### Deploy docker

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible$ ansible-playbook playbooks/dev/main.yaml --diff 
TASK [../../roles/docker : Ensure curl is present (on older systems without SNI).] ***
ok: [web_server]

TASK [../../roles/docker : include_tasks] **************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/docker.yml for web_server

TASK [../../roles/docker : Add Docker apt key.] ********************************
ok: [web_server]

TASK [../../roles/docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [web_server]

TASK [../../roles/docker : Add Docker repository.] *****************************
ok: [web_server]

TASK [../../roles/docker : Install Docker packages.] ***************************
skipping: [web_server]

TASK [../../roles/docker : Install Docker packages (with downgrade option).] ***
ok: [web_server]

TASK [../../roles/docker : Ensure Docker is started and enabled at boot.] ******
ok: [web_server]

TASK [../../roles/docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [../../roles/docker : include_tasks] **************************************
included: /home/quiner/innopolis/dev-ops-course-labs/ansible/roles/docker/tasks/docker-compose.yml for web_server

TASK [../../roles/docker : Check current docker-compose version.] **************
ok: [web_server]

TASK [../../roles/docker : set_fact] *******************************************
ok: [web_server]

TASK [../../roles/docker : Delete existing docker-compose version if it's different.] ***
skipping: [web_server]

TASK [../../roles/docker : Install Docker Compose (if configured).] ************
skipping: [web_server]

TASK [../../roles/docker : Get docker group info using getent.] ****************
skipping: [web_server]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] ***
skipping: [web_server]

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ********

PLAY RECAP *********************************************************************
web_server                 : ok=13   changed=0    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   
```

### Inventory details

```shell
quiner@quiner-MaiBook-X-series:~/innopolis/dev-ops-course-labs/ansible$ ansible-inventory -i inventory/yacloud_compute.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "xxx.xxx.xxx.xxx"
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
            "web_server"
        ]
    }
}
```
