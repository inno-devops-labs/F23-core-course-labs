## Best practices:
 * Use ansible yaml format
 * Use variables
 * Do not put secrets into configs

 # First task
 ```
 k-tyulebaeva$ ansible-playbook playbooks/dev/main.yml
 PLAY [all] *******************************************************************************************************************
 TASK [Gathering Facts] *******************************************************************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.pip : Ensure Pip is installed.] ****************************************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] **********************************************************
 ok: [158.158.92.112] => (item={'name': 'docker'})
 TASK [geerlingguy.docker : Load OS-specific vars.] ***************************************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : include_tasks] ************************************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : include_tasks] ************************************************************************************
 included: /home/k-tyulebaeva/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 158.158.92.112
 TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure dependencies are installed.] ***************************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] **********
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *******************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Add Docker apt key.] ******************************************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *******************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **********************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Add Docker repository.] ***************************************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Install Docker packages.] *************************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Install docker-compose plugin.] *******************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *******************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Configure Docker daemon options.] *****************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ****************************************************
 ok: [158.158.92.112]
 TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ************************************
 TASK [geerlingguy.docker : include_tasks] ************************************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Get docker group info using getent.] **************************************************************
 skipping: [158.158.92.112]
 TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *****************************************
 TASK [geerlingguy.docker : include_tasks] ************************************************************************************
 skipping: [158.158.92.112]
 PLAY RECAP *******************************************************************************************************************
 158.158.92.112            : ok=13   changed=0    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0  
 ```

 Inside the VM:
 ```
 root@fhmv4skgn3aa7q3q3kmf:~# docker --version
 Docker version 24.0.6, build ed223bc
 ```


 # Task 2
 ```
 k-tyulebaeva$ ansible-playbook playbooks/dev/main.yml 
 PLAY [Install docker] ********************************************************************************************************
 TASK [Gathering Facts] *******************************************************************************************************
 ok: [158.158.92.112]
 TASK [../../roles/docker : Ensure old versions of Docker are not installed.] *************************************************
 ok: [158.158.92.112]
 TASK [../../roles/docker : include_tasks] ************************************************************************************
 included: /home/k-tyulebaeva/devops/ansible/roles/docker/tasks/install_docker.yml for 158.158.92.112
 TASK [../../roles/docker : Install packages required by docker] **************************************************************
 ok: [158.158.92.112]
 TASK [../../roles/docker : Add docker GPG key] *******************************************************************************
 ok: [158.158.92.112]
 TASK [../../roles/docker : Add docker apt repo] ******************************************************************************
 ok: [158.158.92.112]
 TASK [../../roles/docker : Install docker] ***********************************************************************************
 ok: [158.158.92.112]
 PLAY RECAP *******************************************************************************************************************
 158.158.92.112            : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
 ```

 #### `ansible-inventory -i inventory/hosts.yml --list`:
 ```
 k-tyulebaeva$ ansible-inventory -i inventory/hosts.yml --list
 {
     "_meta": {
         "hostvars": {
             "158.158.92.112": {
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
             "158.158.92.112"
         ]
     }
 }
 ```

 # Lab6
 ```
 ok: [k-tyulebaeva-instance]
 TASK [docker : Ensure old versions of Docker are not installed.] *************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Install docker] ***********************************************************************************************
 included: /home/ktyulebaeva/devops/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for k-tyulebaeva-instance
 TASK [docker : Install packages required by docker] **************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Add docker GPG key] *******************************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Add docker apt repo] ******************************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Install docker] ***********************************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Install 'Docker SDK for Python'] ******************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Install pip] **************************************************************************************************
 included: /home/ktyulebaeva/devops/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for k-tyulebaeva-instance
 TASK [docker : Install pip] **************************************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [docker : Install docker_compose] ***************************************************************************************
 included: /home/ktyulebaeva/devops/core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for k-tyulebaeva-instance
 TASK [docker : Install Docker Compose] ***************************************************************************************
 ok: [k-tyulebaeva-instance]
 TASK [web_app : Wipe web app] ************************************************************************************************
 included: /home/ktyulebaeva/devops/core-course-labs/ansible/roles/web_app/tasks/wipe_web_app.yml for k-tyulebaeva-instance
 TASK [web_app : Remove moscow-time-app directory] ****************************************************************************
 changed: [k-tyulebaeva-instance]
 TASK [web_app : Remove Docker container] *************************************************************************************
 changed: [k-tyulebaeva-instance]
 TASK [web_app : Remove Docker image] *****************************************************************************************
 changed: [k-tyulebaeva-instance]
 TASK [web_app : Deploy web app] **********************************************************************************************
 included: /home/ktyulebaeva/devops/core-course-labs/ansible/roles/web_app/tasks/deliver_docker_compose_file.yml for k-tyulebaeva-instance
 TASK [web_app : Create moscow-time-app directory] ****************************************************************************
 changed: [k-tyulebaeva-instance]
 TASK [web_app : Deliver docker compose file to /home/ubuntu/moscow-time-app] *************************************************
 changed: [k-tyulebaeva-instance]
 RUNNING HANDLER [web_app : Restart Docker Compose] ***************************************************************************
 changed: [k-tyulebaeva-instance]
 PLAY RECAP *******************************************************************************************************************
 k-tyulebaeva-instance : ok=20   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   