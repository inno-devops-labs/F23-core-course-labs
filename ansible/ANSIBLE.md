# ansible-playbook

```
SSH password:
BECOME password[defaults to SSH password]:

PLAY [yandex_cloud] *******************************************************************************

TASK [Gathering Facts] ****************************************************************************
ok: [vm]

TASK [docker : Load OS-specific vars.] ************************************************************
ok: [vm]

TASK [docker : include_tasks] *********************************************************************
skipping: [vm]

TASK [docker : include_tasks] *********************************************************************
included: /Users/kamil/devops/ansible/roles/docker/tasks/setup-Debian.yml for vm

TASK [docker : Ensure old versions of Docker are not installed.] **********************************
ok: [vm]

TASK [docker : Ensure dependencies are installed.] ************************************************
changed: [vm]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [vm]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ****************
ok: [vm]

TASK [docker : Add Docker apt key.] ***************************************************************
changed: [vm]

TASK [docker : Ensure curl is present (on older systems without SNI).] ****************************
skipping: [vm]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] *******************
skipping: [vm]

TASK [docker : Add Docker repository.] ************************************************************
changed: [vm]

TASK [docker : Install Docker packages.] **********************************************************
skipping: [vm]

TASK [docker : Install Docker packages (with downgrade option).] **********************************
changed: [vm]

TASK [docker : Install docker-compose plugin.] ****************************************************
skipping: [vm]

TASK [docker : Install docker-compose-plugin (with downgrade option).] ****************************
skipping: [vm]

TASK [docker : Ensure /etc/docker/ directory exists.] *********************************************
skipping: [vm]

TASK [docker : Configure Docker daemon options.] **************************************************
skipping: [vm]

TASK [docker : Ensure Docker is started and enabled at boot.] *************************************
ok: [vm]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *********************

RUNNING HANDLER [docker : restart docker] *********************************************************
changed: [vm]

TASK [docker : include_tasks] *********************************************************************
included: /Users/kamil/devops/ansible/roles/docker/tasks/docker-compose.yml for vm

TASK [docker : Check current docker-compose version.] *********************************************
ok: [vm]

TASK [docker : set_fact] **************************************************************************
ok: [vm]

TASK [docker : Delete existing docker-compose version if it's different.] *************************
ok: [vm]

TASK [docker : Install Docker Compose (if configured).] *******************************************
changed: [vm]

TASK [docker : Get docker group info using getent.] ***********************************************
skipping: [vm]

TASK [docker : Check if there are any users to add to the docker group.] **************************
skipping: [vm]

TASK [docker : include_tasks] *********************************************************************
skipping: [vm]

PLAY RECAP ****************************************************************************************
vm                         : ok=16   changed=6    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0

```

# ansible-inventory

```
{
    "_meta": {
        "hostvars": {
            "vm": {
                "ansible_become": true,
                "ansible_host": "localhost",
                "ansible_port": 2222,
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "xdkomel"
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
            "vm"
        ]
    }
}

```
