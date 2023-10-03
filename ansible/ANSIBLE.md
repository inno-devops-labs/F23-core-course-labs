results of first lines of command
```bash
PLAY [Prepare docker] **********************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] **************************************************************************************************************************************************************
included: /home/maruf/study/devops/core-course-labs/ansible/roles/docker/tasks/setup-Debian.yml for localhost

TASK [docker : Ensure old versions of Docker are not installed.] ***************************************************************************************************************************
ok: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...],
    "skip_reason": "Conditional result was False"
}

TASK [docker : Ensure dependencies are installed.] *****************************************************************************************************************************************
ok: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...]
}

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *********************************************************************************************************
ok: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...]
}

TASK [docker : Add Docker apt key.] ********************************************************************************************************************************************************
ok: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...]
}

TASK [docker : Ensure curl is present (on older systems without SNI).] *********************************************************************************************************************
skipping: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...],
    "skip_reason": "Conditional result was False"
}

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ************************************************************************************************************
skipping: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...],
    "skip_reason": "Conditional result was False"
}

TASK [docker : Add Docker repository.] *****************************************************************************************************************************************************
ok: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...]
}

TASK [docker : include_tasks] **************************************************************************************************************************************************************
included: /home/maruf/study/devops/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install Docker packages.] ***************************************************************************************************************************************************
skipping: [localhost] => (item=[...]) => {
    "ansible_loop_var": "item",
    "item": [...],
    "skip_reason": "Conditional result was False"
}

TASK [docker : Ensure /etc/docker/ directory exists.] **************************************************************************************************************************************
skipping: [localhost]
```