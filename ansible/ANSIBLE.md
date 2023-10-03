
### Task1: 

Result of the command: ```ansible-playbook playbooks/dev/main.yml```:
```
PLAY [vk_cloud] *********************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************
ok: [89.208.85.212]

TASK [docker : Load OS-specific vars.] **********************************************************************************************************
ok: [89.208.85.212]

TASK [docker : include_tasks] *******************************************************************************************************************
skipping: [89.208.85.212]

TASK [docker : include_tasks] *******************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/setup-Debian.yml for 89.208.85.212

TASK [docker : Ensure old versions of Docker are not installed.] ********************************************************************************
ok: [89.208.85.212]

TASK [docker : Ensure dependencies are installed.] **********************************************************************************************
ok: [89.208.85.212]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *****************************************
skipping: [89.208.85.212]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **************************************************************
ok: [89.208.85.212]

TASK [docker : Add Docker apt key.] *************************************************************************************************************
changed: [89.208.85.212]

TASK [docker : Ensure curl is present (on older systems without SNI).] **************************************************************************
skipping: [89.208.85.212]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] *****************************************************************
skipping: [89.208.85.212]

TASK [docker : Add Docker repository.] **********************************************************************************************************
changed: [89.208.85.212]

TASK [docker : Install Docker packages.] ********************************************************************************************************
skipping: [89.208.85.212]

TASK [docker : Install Docker packages (with downgrade option).] ********************************************************************************
changed: [89.208.85.212]

TASK [docker : Install docker-compose plugin.] **************************************************************************************************
skipping: [89.208.85.212]

TASK [docker : Install docker-compose-plugin (with downgrade option).] **************************************************************************
changed: [89.208.85.212]

TASK [docker : Ensure /etc/docker/ directory exists.] *******************************************************************************************
skipping: [89.208.85.212]

TASK [docker : Configure Docker daemon options.] ************************************************************************************************
skipping: [89.208.85.212]

TASK [docker : Ensure Docker is started and enabled at boot.] ***********************************************************************************
ok: [89.208.85.212]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *******************************************************************

RUNNING HANDLER [docker : restart docker] *******************************************************************************************************
changed: [89.208.85.212]

TASK [docker : include_tasks] *******************************************************************************************************************
skipping: [89.208.85.212]

TASK [docker : Get docker group info using getent.] *********************************************************************************************
skipping: [89.208.85.212]

TASK [docker : Check if there are any users to add to the docker group.] ************************************************************************
skipping: [89.208.85.212]

TASK [docker : include_tasks] *******************************************************************************************************************
skipping: [89.208.85.212]

PLAY RECAP **************************************************************************************************************************************
89.208.85.212              : ok=12   changed=5    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
```


### Task2: 

Result of the command ```ansible-playbook playbooks/dev/main.yml --dif```:

```
PLAY [vk_cloud] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [146.185.243.178]

TASK [docker : Execute apt update] *********************************************
changed: [146.185.243.178]

TASK [docker : include_tasks] **************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 146.185.243.178

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************
ok: [146.185.243.178]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 146.185.243.178

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***
ok: [146.185.243.178]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************
ok: [146.185.243.178]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***
ok: [146.185.243.178]

TASK [geerlingguy.docker : Add Docker apt key.] ********************************
ok: [146.185.243.178]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
ok: [146.185.243.178]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
ok: [146.185.243.178]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [146.185.243.178]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [146.185.243.178]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [146.185.243.178]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [146.185.243.178]

TASK [docker : include_tasks] **************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for 146.185.243.178

TASK [geerlingguy.pip : Ensure Pip is installed.] ******************************
ok: [146.185.243.178]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] ************
ok: [146.185.243.178] => (item={'name': 'docker'})
ok: [146.185.243.178] => (item={'name': 'docker-compose'})

PLAY RECAP *********************************************************************
146.185.243.178            : ok=15   changed=1    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0   
```


Result of the command ```ansible-inventory -i inventory/default_aws_ec2.yml --list```

```
{
    "_meta": {
        "hostvars": {
            "146.185.243.178": {
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vk_cloud"
        ]
    },
    "vk_cloud": {
        "hosts": [
            "146.185.243.178"
        ]
    }
}
```