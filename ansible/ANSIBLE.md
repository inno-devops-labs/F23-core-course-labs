## Ansible commands output (with dynamic inventory)
### Output of `ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yml --diff`
```
PLAY [lab5] *****************************************************************************

TASK [Gathering Facts] ******************************************************************
ok: [devopscourse]

TASK [docker_custom : include_tasks] ****************************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker_custom/tasks/install_pip.yml for devopscourse

TASK [docker_custom : Update apt cache.] ************************************************
ok: [devopscourse]

TASK [docker_custom : Install pip.] *****************************************************
ok: [devopscourse]

TASK [docker_custom : include_tasks] ****************************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker_custom/tasks/install_docker.yml for devopscourse

TASK [geerlingguy.docker : Load OS-specific vars.] **************************************
ok: [devopscourse]

TASK [geerlingguy.docker : include_tasks] ***********************************************
skipping: [devopscourse]

TASK [geerlingguy.docker : include_tasks] ***********************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for devopscourse

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ************
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **************************
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***
ok: [devopscourse]

TASK [geerlingguy.docker : Add Docker apt key.] *****************************************
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ******
skipping: [devopscourse]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : Add Docker repository.] **************************************
ok: [devopscourse]

TASK [geerlingguy.docker : Install Docker packages.] ************************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ************
ok: [devopscourse]

TASK [geerlingguy.docker : Install docker-compose plugin.] ******************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ******
skipping: [devopscourse]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***********************
skipping: [devopscourse]

TASK [geerlingguy.docker : Configure Docker daemon options.] ****************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***************
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] ***********************************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Get docker group info using getent.] *************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ****
skipping: [devopscourse]

TASK [geerlingguy.docker : include_tasks] ***********************************************
skipping: [devopscourse]

TASK [docker_custom : include_tasks] ****************************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker_custom/tasks/install_docker_compose.yml for devopscourse

TASK [geerlingguy.pip : Ensure Pip is installed.] ***************************************
ok: [devopscourse]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] *********************
ok: [devopscourse] => (item={'name': 'docker-compose'})

PLAY RECAP ******************************************************************************
devopscourse               : ok=17   changed=0    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```

### Output of `ansible-inventory -i inventory/yacloud_compute.yml --list`
```
{
    "_meta": {
        "hostvars": {
            "devopscourse": {
                "ansible_host": "84.201.129.17",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
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
            "devopscourse"
        ]
    }
}
```


## Ansible commands output (lab 6 = web_app role + dynamic inventory)
`ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/app_python/main.yml`
```
PLAY [Deploy Python web application] *******************************************

TASK [Gathering Facts] *********************************************************
ok: [devopscourse]

TASK [docker_custom : include_tasks] *******************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker_custom/tasks/install_pip.yml for devopscourse

TASK [docker_custom : Update apt cache.] ***************************************
ok: [devopscourse]

TASK [docker_custom : Install pip.] ********************************************
ok: [devopscourse]

TASK [docker_custom : include_tasks] *******************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker_custom/tasks/install_docker.yml for devopscourse

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************
ok: [devopscourse]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [devopscourse]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for devopscourse

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***
ok: [devopscourse]

TASK [geerlingguy.docker : Add Docker apt key.] ********************************
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
ok: [devopscourse]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
ok: [devopscourse]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [devopscourse]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [devopscourse]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [devopscourse]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [devopscourse]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [devopscourse]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [devopscourse]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [devopscourse]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [devopscourse]

TASK [docker_custom : include_tasks] *******************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker_custom/tasks/install_docker_compose.yml for devopscourse

TASK [geerlingguy.pip : Ensure Pip is installed.] ******************************
ok: [devopscourse]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] ************
ok: [devopscourse] => (item={'name': 'docker-compose'})

TASK [web_app : Deploy application.] *******************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/web_app/tasks/deploy.yml for devopscourse

TASK [web_app : Create application directory.] *********************************
changed: [devopscourse]

TASK [web_app : Fill template and transfer docker-compose.yml .] ***************
changed: [devopscourse]

TASK [web_app : Run docker-compose.] *******************************************
changed: [devopscourse]

TASK [web_app : Wipe application.] *********************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for devopscourse

TASK [web_app : Stop docker-compose containers and remove images.] *************
changed: [devopscourse]

TASK [web_app : Remove application directory.] *********************************
changed: [devopscourse]

PLAY RECAP *********************************************************************
devopscourse               : ok=24   changed=5    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```
