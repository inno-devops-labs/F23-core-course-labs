## Lab 5

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


## Lab 6

### Task 1

Result of command ```ansible-playbook playbooks/dev/python/main.yml```:

```
PLAY [vk_cloud] *********************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************
ok: [89.208.196.134]

TASK [docker : Execute apt update] **************************************************************************************************************
changed: [89.208.196.134]

TASK [docker : include_tasks] *******************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 89.208.196.134

TASK [geerlingguy.docker : Load OS-specific vars.] **********************************************************************************************
ok: [89.208.196.134]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 89.208.196.134

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ********************************************************************
ok: [89.208.196.134]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **********************************************************************************
ok: [89.208.196.134]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *****************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **************************************************
ok: [89.208.196.134]

TASK [geerlingguy.docker : Add Docker apt key.] *************************************************************************************************
changed: [89.208.196.134]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *****************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Add Docker repository.] **********************************************************************************************
changed: [89.208.196.134]

TASK [geerlingguy.docker : Install Docker packages.] ********************************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ********************************************************************
changed: [89.208.196.134]

TASK [geerlingguy.docker : Install docker-compose plugin.] **************************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *******************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Configure Docker daemon options.] ************************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***********************************************************************
ok: [89.208.196.134]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *******************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] *******************************************************************************************
changed: [89.208.196.134]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Get docker group info using getent.] *********************************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ************************************************************
skipping: [89.208.196.134]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
skipping: [89.208.196.134]

TASK [docker : include_tasks] *******************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for 89.208.196.134

TASK [geerlingguy.pip : Ensure Pip is installed.] ***********************************************************************************************
changed: [89.208.196.134]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] *****************************************************************************
changed: [89.208.196.134] => (item={'name': 'docker'})
changed: [89.208.196.134] => (item={'name': 'docker-compose'})

TASK [web_app : Install application] ************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/web_app/tasks/run.yml for 89.208.196.134

TASK [web_app : Create a directory if it does not exist] ****************************************************************************************
changed: [89.208.196.134]

TASK [web_app : Create docker-compose] **********************************************************************************************************
changed: [89.208.196.134]

TASK [web_app : Run application] ****************************************************************************************************************
fatal: [89.208.196.134]: FAILED! => {"changed": false, "errors": [], "module_stderr": "Creating wildqueue_time_1 ... \nCreating wildqueue_time_1 ... error\n", "module_stdout": "tagname: Pulling from wildqueue/devops-hw\nDigest: sha256:9b2f256fa1b43de04749114504844b3934843a769a84bf8dcd8a663ea9edf1c9\nStatus: Downloaded newer image for wildqueue/devops-hw:tagname\n", "msg": "Error starting project Encountered errors while bringing up the project."}

PLAY RECAP **************************************************************************************************************************************
89.208.196.134             : ok=19   changed=9    unreachable=0    failed=1    skipped=13   rescued=0    ignored=0   

egor@egor-Swift-SF314-43:~/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible$ ansible-playbook playbooks/dev/python/main.yml

PLAY [vk_cloud] *********************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************
The authenticity of host '37.139.33.96 (37.139.33.96)' can't be established.
ED25519 key fingerprint is SHA256:oyp4Pdj+rGT1QEXvQDOzBjJs9GMPDJUW9LZ0/WXP9zc.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [37.139.33.96]

TASK [docker : Execute apt update] **************************************************************************************************************
changed: [37.139.33.96]

TASK [docker : include_tasks] *******************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 37.139.33.96

TASK [geerlingguy.docker : Load OS-specific vars.] **********************************************************************************************
ok: [37.139.33.96]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 37.139.33.96

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ********************************************************************
ok: [37.139.33.96]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **********************************************************************************
ok: [37.139.33.96]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *****************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **************************************************
ok: [37.139.33.96]

TASK [geerlingguy.docker : Add Docker apt key.] *************************************************************************************************
changed: [37.139.33.96]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *****************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Add Docker repository.] **********************************************************************************************
changed: [37.139.33.96]

TASK [geerlingguy.docker : Install Docker packages.] ********************************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ********************************************************************
changed: [37.139.33.96]

TASK [geerlingguy.docker : Install docker-compose plugin.] **************************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *******************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Configure Docker daemon options.] ************************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***********************************************************************
ok: [37.139.33.96]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *******************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] *******************************************************************************************
changed: [37.139.33.96]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Get docker group info using getent.] *********************************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ************************************************************
skipping: [37.139.33.96]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************
skipping: [37.139.33.96]

TASK [docker : include_tasks] *******************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for 37.139.33.96

TASK [geerlingguy.pip : Ensure Pip is installed.] ***********************************************************************************************
changed: [37.139.33.96]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] *****************************************************************************
changed: [37.139.33.96] => (item={'name': 'docker'})
changed: [37.139.33.96] => (item={'name': 'docker-compose'})

TASK [web_app : Install application] ************************************************************************************************************
included: /home/egor/InnoSubjects/F23/DevOps/devops-core-course-labs/ansible/roles/web_app/tasks/run.yml for 37.139.33.96

TASK [web_app : Create a directory if it does not exist] ****************************************************************************************
changed: [37.139.33.96]

TASK [web_app : Create docker-compose] **********************************************************************************************************
changed: [37.139.33.96]

TASK [web_app : Run application] ****************************************************************************************************************
changed: [37.139.33.96]

PLAY RECAP **************************************************************************************************************************************
37.139.33.96               : ok=20   changed=10   unreachable=0    failed=0    skipped=13   rescued=0    ignored=0   
```