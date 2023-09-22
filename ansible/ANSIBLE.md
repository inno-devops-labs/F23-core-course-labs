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

# Lab 6

## Python tasks

```yaml
playbook: playbooks/dev/app_python.yml

  play #1 (all): lab6 python	TAGS: []
    tasks:
      docker : Execute apt update	TAGS: [docker, web_app-python]
      geerlingguy.pip : Ensure Pip is installed.	TAGS: [docker, web_app-python]
      geerlingguy.pip : Ensure pip_install_packages are installed.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Load OS-specific vars.	TAGS: [docker, web_app-python]
      include_tasks	TAGS: [docker, web_app-python]
      include_tasks	TAGS: [docker, web_app-python]
      geerlingguy.docker : Install Docker packages.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Install Docker packages (with downgrade option).	TAGS: [docker, web_app-python]
      geerlingguy.docker : Install docker-compose plugin.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Install docker-compose-plugin (with downgrade option).	TAGS: [docker, web_app-python]
      geerlingguy.docker : Ensure /etc/docker/ directory exists.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Configure Docker daemon options.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Ensure Docker is started and enabled at boot.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.	TAGS: [docker, web_app-python]
      include_tasks	TAGS: [docker, web_app-python]
      geerlingguy.docker : Get docker group info using getent.	TAGS: [docker, web_app-python]
      geerlingguy.docker : Check if there are any users to add to the docker group.	TAGS: [docker, web_app-python]
      include_tasks	TAGS: [docker, web_app-python]
      web_app : Check if docker-compose.yml file exists	TAGS: [web_app-python, webapp, webapp-wipe]
      web_app : Check if Web App directory exists	TAGS: [web_app-python, webapp, webapp-wipe]
      web_app : Docker Compose remove	TAGS: [web_app-python, webapp, webapp-wipe]
      web_app : Remove directory {{ web_app_path }}	TAGS: [web_app-python, webapp, webapp-wipe]
      web_app : Create directory {{ web_app_path }}	TAGS: [web_app-python, webapp, webapp-install]
      web_app : Template Docker Compose configuration	TAGS: [web_app-python, webapp, webapp-install]
      web_app : Pull images	TAGS: [web_app-python, webapp, webapp-install]
```

### ansible-playbook -i inventory/yacloud_compute.yml  playbooks/dev/app_python.yml -e web_app_full_wipe=true | tail -n 50

```yaml
TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [test]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [test]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [test]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [test]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [test]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [test]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [test]

TASK [web_app : Check if docker-compose.yml file exists] ***********************
ok: [test]

TASK [web_app : Check if Web App directory exists] *****************************
ok: [test]

TASK [web_app : Docker Compose remove] *****************************************
changed: [test]

TASK [web_app : Remove directory /app_python] **********************************
changed: [test]

TASK [web_app : Create directory /app_python] **********************************
changed: [test]

TASK [web_app : Template Docker Compose configuration] *************************
changed: [test]

TASK [web_app : Pull images] ***************************************************
changed: [test]

RUNNING HANDLER [web_app : Web App Docker Compose restart] *********************
changed: [test]

PLAY RECAP *********************************************************************
test                       : ok=21   changed=7    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```

## Rust tasks

```yaml
playbook: playbooks/dev/app_rust.yml

  play #1 (all): lab6 rust	TAGS: []
    tasks:
      docker : Execute apt update	TAGS: [docker, web_app-rust]
      geerlingguy.pip : Ensure Pip is installed.	TAGS: [docker, web_app-rust]
      geerlingguy.pip : Ensure pip_install_packages are installed.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Load OS-specific vars.	TAGS: [docker, web_app-rust]
      include_tasks	TAGS: [docker, web_app-rust]
      include_tasks	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Install Docker packages.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Install Docker packages (with downgrade option).	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Install docker-compose plugin.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Install docker-compose-plugin (with downgrade option).	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Ensure /etc/docker/ directory exists.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Configure Docker daemon options.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Ensure Docker is started and enabled at boot.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.	TAGS: [docker, web_app-rust]
      include_tasks	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Get docker group info using getent.	TAGS: [docker, web_app-rust]
      geerlingguy.docker : Check if there are any users to add to the docker group.	TAGS: [docker, web_app-rust]
      include_tasks	TAGS: [docker, web_app-rust]
      web_app : Check if docker-compose.yml file exists	TAGS: [web_app-rust, webapp, webapp-wipe]
      web_app : Check if Web App directory exists	TAGS: [web_app-rust, webapp, webapp-wipe]
      web_app : Docker Compose remove	TAGS: [web_app-rust, webapp, webapp-wipe]
      web_app : Remove directory {{ web_app_path }}	TAGS: [web_app-rust, webapp, webapp-wipe]
      web_app : Create directory {{ web_app_path }}	TAGS: [web_app-rust, webapp, webapp-install]
      web_app : Template Docker Compose configuration	TAGS: [web_app-rust, webapp, webapp-install]
      web_app : Pull images	TAGS: [web_app-rust, webapp, webapp-install]
```

### ansible-playbook -i inventory/yacloud_compute.yml  playbooks/dev/app_rust.yml -e web_app_full_wipe=true | tail -n 50

```yaml
TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [test]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [test]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [test]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [test]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [test]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [test]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [test]

TASK [web_app : Check if docker-compose.yml file exists] ***********************
ok: [test]

TASK [web_app : Check if Web App directory exists] *****************************
ok: [test]

TASK [web_app : Docker Compose remove] *****************************************
changed: [test]

TASK [web_app : Remove directory /app_rust] ************************************
changed: [test]

TASK [web_app : Create directory /app_rust] ************************************
changed: [test]

TASK [web_app : Template Docker Compose configuration] *************************
changed: [test]

TASK [web_app : Pull images] ***************************************************
changed: [test]

RUNNING HANDLER [web_app : Web App Docker Compose restart] *********************
changed: [test]

PLAY RECAP *********************************************************************
test                       : ok=21   changed=7    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```
