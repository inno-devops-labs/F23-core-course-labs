### Existing docker role

`ansible-playbook -i ansible/inventory/main.yml ansible/playbooks/dev/main.yml`

```
PLAY [Deploy Docker using Ansible Galaxy Role] **********************************************************************************

TASK [Gathering Facts] **********************************************************************************************************
ok: [webserver1]

TASK [geerlingguy.docker : Load OS-specific vars.] ******************************************************************************
ok: [webserver1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************
included: /home/newjazz/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for webserver1

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ****************************************************
ok: [webserver1]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ******************************************************************
changed: [webserver1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *************
skipping: [webserver1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **********************************
ok: [webserver1]

TASK [geerlingguy.docker : Add Docker apt key.] *********************************************************************************
changed: [webserver1]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **********************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Add Docker repository.] ******************************************************************************
changed: [webserver1]

TASK [geerlingguy.docker : Install Docker packages.] ****************************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****************************************************
changed: [webserver1]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************
ok: [webserver1]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************
ok: [webserver1]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ***************************************************************************
changed: [webserver1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************
skipping: [webserver1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************
skipping: [webserver1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************
skipping: [webserver1]

PLAY RECAP **********************************************************************************************************************
webserver1                 : ok=12   changed=5    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```

### Custom

`ansible-playbook -i ansible/inventory/main.yml ansible/playbooks/dev/custom.yml`

```

```

### Inventory details

```
{
    "_meta": {
        "hostvars": {
            "webserver1": {
                "ansible_become_method": "",
                "ansible_become_pass": "",
                "ansible_host": "",
                "ansible_ssh_port": 22,
                "ansible_user": ""
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
            "webserver1"
        ]
    }
}
```