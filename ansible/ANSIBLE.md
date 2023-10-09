Best practices:

* Keep all simple
* Use ansible yaml format
* Use variables
* Use dynamic inventory
* Do not put secrets into configs
* Use roles instead of a lot of includes

# Lab 5
# First task

```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/ansible$ ansible-playbook playbooks/dev/main.yml

PLAY [all] *******************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************
ok: [158.160.107.107]

TASK [geerlingguy.pip : Ensure Pip is installed.] ****************************************************************************
ok: [158.160.107.107]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] **********************************************************
ok: [158.160.107.107] => (item={'name': 'docker'})

TASK [geerlingguy.docker : Load OS-specific vars.] ***************************************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************
included: /home/edikgoose/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 158.160.107.107

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ***************************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] **********
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *******************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Add Docker apt key.] ******************************************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *******************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **********************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Add Docker repository.] ***************************************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Install Docker packages.] *************************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Install docker-compose plugin.] *******************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *******************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Configure Docker daemon options.] *****************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ****************************************************
ok: [158.160.107.107]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ************************************

TASK [geerlingguy.docker : include_tasks] ************************************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Get docker group info using getent.] **************************************************************
skipping: [158.160.107.107]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *****************************************

TASK [geerlingguy.docker : include_tasks] ************************************************************************************
skipping: [158.160.107.107]

PLAY RECAP *******************************************************************************************************************
158.160.107.107            : ok=13   changed=0    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0  
```

Inside the VM:

```
root@fhmv4skgn3aa7q3q3kmf:~# docker --version
Docker version 24.0.6, build ed223bc
```

# Task 2

```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/ansible$ ansible-playbook playbooks/dev/main.yml 

PLAY [Install docker] ********************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************
ok: [158.160.107.107]

TASK [../../roles/docker : Ensure old versions of Docker are not installed.] *************************************************
ok: [158.160.107.107]

TASK [../../roles/docker : include_tasks] ************************************************************************************
included: /home/edikgoose/iu-devops/ansible/roles/docker/tasks/install_docker.yml for 158.160.107.107

TASK [../../roles/docker : Install packages required by docker] **************************************************************
ok: [158.160.107.107]

TASK [../../roles/docker : Add docker GPG key] *******************************************************************************
ok: [158.160.107.107]

TASK [../../roles/docker : Add docker apt repo] ******************************************************************************
ok: [158.160.107.107]

TASK [../../roles/docker : Install docker] ***********************************************************************************
ok: [158.160.107.107]

PLAY RECAP *******************************************************************************************************************
158.160.107.107            : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

#### `ansible-inventory -i inventory/hosts.yml --list`:

```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/ansible$ ansible-inventory -i inventory/hosts.yml --list
{
    "_meta": {
        "hostvars": {
            "158.160.107.107": {
                "private_key_file_yandex": "~/.ssh/id_ed25519-cloud",
                "remote_user_yandex": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandexcloudvm"
        ]
    },
    "yandexcloudvm": {
        "hosts": [
            "158.160.107.107"
        ]
    }
}
```

#### After add dynamic inventory:
```
edikgoose@edikgoose-NBLB-WAX9N:~/iu-devops/ansible$ ansible-inventory --list
{
    "_meta": {
        "hostvars": {
            "edikgoose-compute-instance": {
                "ansible_host": "51.250.91.0"
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
            "edikgoose-compute-instance"
        ]
    }
}
```


# Lab 6
```
ok: [edikgoose-compute-instance]

TASK [docker : Ensure old versions of Docker are not installed.] *************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Install docker] ***********************************************************************************************
included: /home/edikgoose/iu-devops/ansible/roles/docker/tasks/install_docker.yml for edikgoose-compute-instance

TASK [docker : Install packages required by docker] **************************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Add docker GPG key] *******************************************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Add docker apt repo] ******************************************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Install docker] ***********************************************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Install 'Docker SDK for Python'] ******************************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Install pip] **************************************************************************************************
included: /home/edikgoose/iu-devops/ansible/roles/docker/tasks/install_pip.yml for edikgoose-compute-instance

TASK [docker : Install pip] **************************************************************************************************
ok: [edikgoose-compute-instance]

TASK [docker : Install docker_compose] ***************************************************************************************
included: /home/edikgoose/iu-devops/ansible/roles/docker/tasks/install_docker_compose.yml for edikgoose-compute-instance

TASK [docker : Install Docker Compose] ***************************************************************************************
ok: [edikgoose-compute-instance]

TASK [web_app : Wipe web app] ************************************************************************************************
included: /home/edikgoose/iu-devops/ansible/roles/web_app/tasks/wipe_web_app.yml for edikgoose-compute-instance

TASK [web_app : Remove moscow-time-app directory] ****************************************************************************
changed: [edikgoose-compute-instance]

TASK [web_app : Remove Docker container] *************************************************************************************
changed: [edikgoose-compute-instance]

TASK [web_app : Remove Docker image] *****************************************************************************************
changed: [edikgoose-compute-instance]

TASK [web_app : Deploy web app] **********************************************************************************************
included: /home/edikgoose/iu-devops/ansible/roles/web_app/tasks/deliver_docker_compose_file.yml for edikgoose-compute-instance

TASK [web_app : Create moscow-time-app directory] ****************************************************************************
changed: [edikgoose-compute-instance]

TASK [web_app : Deliver docker compose file to /home/ubuntu/moscow-time-app] *************************************************
changed: [edikgoose-compute-instance]

RUNNING HANDLER [web_app : Restart Docker Compose] ***************************************************************************
changed: [edikgoose-compute-instance]

PLAY RECAP *******************************************************************************************************************
edikgoose-compute-instance : ok=20   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```