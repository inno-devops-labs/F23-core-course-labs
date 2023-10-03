

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