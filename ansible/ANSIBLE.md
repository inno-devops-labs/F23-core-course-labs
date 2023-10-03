# Lab 5


## Task 1
### Repository structure

My project tree:

```sh
.
├── ansible
│   ├── ansible.cfg
│   ├── ANSIBLE.md
│   ├── inventory
│   │   ├── inventory.yaml
│   │   └── yacloud_compute.yaml
│   ├── playbooks
│   │   └── dev
│   │       └── main.yaml
│   └── roles
│       ├── docker
│       │   ├── defaults
│       │   │   └── main.yml
│       │   ├── files
│       │   ├── handlers
│       │   │   └── main.yml
│       │   ├── meta
│       │   │   └── main.yml
│       │   ├── README.md
│       │   ├── tasks
│       │   │   └── main.yml
│       │   ├── templates
│       │   ├── tests
│       │   │   ├── inventory
│       │   │   └── test.yml
│       │   └── vars
│       │       └── main.yml
│       └── web_app
│           ├── defaults
│           │   └── main.yml
│           ├── files
│           ├── handlers
│           │   └── main.yml
│           ├── meta
│           │   └── main.yml
│           ├── README.md
│           ├── tasks
│           │   └── main.yml
│           ├── templates
│           ├── tests
│           │   ├── inventory
│           │   └── test.yml
│           └── vars
│               └── main.yml
├── app_go
├── app_python
└── terraform
```

### Using Existing Ansible Role:

```yaml
---
- hosts: all
  become: true
  roles:
    - geerlingguy.docker
    # - roles/docker
  post_tasks:
    # below we check results of a role execution
    - name: Verify docker installation
      command: docker --version
      register: docker_version

    - name: Print docker version
      debug:
        msg: "{{ docker_version.stdout }}"
```

### Create a Playbook and Testing the Existing Role

```sh
$ ansible-playbook -i inventory/inventory.yaml playbooks/dev/main.yaml -e "ansible_ssh_user=ubuntu" --private-key ~/.ssh/id_ed25519

PLAY [all] ****************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Load OS-specific vars.] ************************************************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : include_tasks] *********************************************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : include_tasks] *********************************************************************
included: /home/artem/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for docker_installer_testbed

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] **********************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ************************************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ****************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Add Docker apt key.] ***************************************************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ****************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *******************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Add Docker repository.] ************************************************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Install Docker packages.] **********************************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] **********************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Install docker-compose plugin.] ****************************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ****************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *********************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Configure Docker daemon options.] **************************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *************************************
ok: [docker_installer_testbed]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *********************

TASK [geerlingguy.docker : include_tasks] *********************************************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Get docker group info using getent.] ***********************************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **************************
skipping: [docker_installer_testbed]

TASK [geerlingguy.docker : include_tasks] *********************************************************************
skipping: [docker_installer_testbed]

TASK [Verify docker installation] *****************************************************************************
changed: [docker_installer_testbed]

TASK [Print docker version] ***********************************************************************************
ok: [docker_installer_testbed] => {
    "msg": "Docker version 24.0.6, build ed223bc"
}

PLAY RECAP ****************************************************************************************************
docker_installer_testbed   : ok=13   changed=1    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
```

## Task 2: Custom Docker Role
### Custom Docker Role:

Below I'm using my own Docker provisioning role, located at `ansible/roles/docker`

## Deployment Output

```sh
$ ansible-playbook -i inventory/inventory.yaml playbooks/dev/main.yaml --private-key ~/.ssh/id_ed25519 --diff

PLAY [all] *********************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [docker_installer_testbed]

TASK [docker : Install pip] ****************************************************************************************************************************************************
ok: [docker_installer_testbed]

TASK [docker : Verify pip installation] ****************************************************************************************************************************************
changed: [docker_installer_testbed]

TASK [docker : pip version] ****************************************************************************************************************************************************
ok: [docker_installer_testbed] => {
    "msg": "pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)"
}

TASK [docker : Install docker] *************************************************************************************************************************************************
ok: [docker_installer_testbed]

TASK [docker : Verify docker installation] *************************************************************************************************************************************
changed: [docker_installer_testbed]

TASK [docker : docker version] *************************************************************************************************************************************************
ok: [docker_installer_testbed] => {
    "msg": "Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1"
}

TASK [docker : Install docker-compose] *****************************************************************************************************************************************
ok: [docker_installer_testbed]

TASK [docker : Verify docker-compose installation] *****************************************************************************************************************************
changed: [docker_installer_testbed]

TASK [docker : docker-compose version] *****************************************************************************************************************************************
ok: [docker_installer_testbed] => {
    "msg": "docker-compose version 1.29.2, build unknown"
}

PLAY RECAP *********************************************************************************************************************************************************************
docker_installer_testbed   : ok=10   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details

```sh
$ ansible-inventory -i inventory/inventory.yaml --list
{
    "_meta": {
        "hostvars": {
            "docker_installer_testbed": {
                "ansible_connection": "ssh",
                "ansible_host": "158.XXX.XXX.XXX",
                "ansible_port": 22,
                "ansible_ssh_options": "-o StrictHostKeyChecking=no",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "servers"
        ]
    },
    "servers": {
        "hosts": [
            "docker_installer_testbed"
        ]
    }
}
```

Also, the deployed application works:
![app response](https://i.imgur.com/UQLr7pz.png)

## Bonus Task

We need to use yandex compute cloud dynamic inventory to get this working on Yandex Cloud.
I have put the dynamic inventory plugin `yacloud_compute.py` into `~/.ansible/plugins/inventory/` and the config into `ansible/inventory/yacloud_compute.yaml`, where we need to specify oauth token for yandex cloud.

Check if the dynamic inventory works:

```sh
$ ansible-inventory -i inventory/yacloud_compute.yaml --graph
@all:
  |--@ungrouped:
  |--@yacloud:
  |  |--terraform-vm
```

Here we can see my virtual machine `terraform-vm`

So, we can launch our playbook with dynamic inventory:

```sh
$ ansible-playbook -i inv
entory/yacloud_compute.yaml playbooks/dev/main.yaml -e "ansible_ssh_user=ubuntu" --private-key ~/.ssh/id_ed2551
9

PLAY [all] ****************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************
ok: [terraform-vm]

TASK [docker : Install pip] ***********************************************************************************
changed: [terraform-vm]

TASK [docker : Verify pip installation] ***********************************************************************
changed: [terraform-vm]

TASK [docker : pip version] ***********************************************************************************
ok: [terraform-vm] => {
    "msg": "pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)"
}

TASK [docker : Install docker] ********************************************************************************
changed: [terraform-vm]

TASK [docker : Verify docker installation] ********************************************************************
changed: [terraform-vm]

TASK [docker : docker version] ********************************************************************************
ok: [terraform-vm] => {
    "msg": "Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1"
}

TASK [docker : Install docker-compose] ************************************************************************
changed: [terraform-vm]

TASK [docker : Verify docker-compose installation] ************************************************************
changed: [terraform-vm]

TASK [docker : docker-compose version] ************************************************************************
ok: [terraform-vm] => {
    "msg": "docker-compose version 1.29.2, build unknown"
}

PLAY RECAP ****************************************************************************************************
terraform-vm               : ok=10   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```