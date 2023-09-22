# Lab 5

## Docker role

### ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/docker.yml

```yaml
PLAY [lab5] **********************************************************************************************************************************************
skipping: no hosts matched

PLAY RECAP ***********************************************************************************************************************************************

[user@fedora ansible]$ ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/docker.yml

PLAY [lab5] **********************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [test]

TASK [docker : Execute apt update] ***********************************************************************************************************************
changed: [test]

TASK [geerlingguy.pip : Ensure Pip is installed.] ********************************************************************************************************
changed: [test]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] **************************************************************************************
changed: [test] => (item={'name': 'docker'})
changed: [test] => (item={'name': 'docker-compose'})

TASK [geerlingguy.docker : Load OS-specific vars.] *******************************************************************************************************
ok: [test]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************
included: /home/user/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for test

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *****************************************************************************
ok: [test]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *******************************************************************************************
changed: [test]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] **************************************
skipping: [test]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***********************************************************
ok: [test]

TASK [geerlingguy.docker : Add Docker apt key.] **********************************************************************************************************
changed: [test]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***********************************************************************
skipping: [test]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **************************************************************
skipping: [test]

TASK [geerlingguy.docker : Add Docker repository.] *******************************************************************************************************
changed: [test]

TASK [geerlingguy.docker : Install Docker packages.] *****************************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *****************************************************************************
changed: [test]

TASK [geerlingguy.docker : Install docker-compose plugin.] ***********************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***********************************************************************
skipping: [test]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ****************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : Configure Docker daemon options.] *********************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ********************************************************************************
ok: [test]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ****************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ****************************************************************************************************
changed: [test]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : Get docker group info using getent.] ******************************************************************************************
skipping: [test]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *********************************************************************
skipping: [test]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************************************
skipping: [test]

PLAY RECAP ***********************************************************************************************************************************************
test                       : ok=14   changed=8    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```

### ansible-inventory -i inventory/yacloud_compute.yml --list

```yaml
{
    "_meta": {
        "hostvars": {
            "test": {
                "ansible_host": "158.160.35.199",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "ubuntu"
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
            "test"
        ]
    }
}
```
