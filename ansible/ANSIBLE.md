
# Outputs

    ansible-playbook ./playbooks/dev/app_python/main.yaml

    PLAY [health check] ********************************************************************************************************************************************************

    TASK [Gathering Facts] *****************************************************************************************************************************************************
    ok: [host1]
    ok: [host2]

    TASK [Ping all hosts] ******************************************************************************************************************************************************
    ok: [host2]
    ok: [host1]

    TASK [Update all apt packages] *********************************************************************************************************************************************
    changed: [host2]
    changed: [host1]

    PLAY [Deploy geerlingguy.docker] *******************************************************************************************************************************************

    TASK [Gathering Facts] *****************************************************************************************************************************************************
    ok: [host1]
    ok: [host2]

    TASK [geerlingguy.docker : Load OS-specific vars.] *************************************************************************************************************************
    ok: [host1]
    ok: [host2]

    TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
    included: /home/jaffart/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for host1, host2

    TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***********************************************************************************************
    ok: [host2]
    ok: [host1]

    TASK [geerlingguy.docker : Ensure dependencies are installed.] *************************************************************************************************************
    changed: [host1]
    changed: [host2]

    TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ********************************************************
    changed: [host1]
    changed: [host2]

    TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *****************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Add Docker apt key.] ****************************************************************************************************************************
    changed: [host2]
    changed: [host1]

    TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *****************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ********************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Add Docker repository.] *************************************************************************************************************************
    changed: [host1]
    changed: [host2]

    TASK [geerlingguy.docker : Install Docker packages.] ***********************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***********************************************************************************************
    changed: [host1]
    changed: [host2]

    TASK [geerlingguy.docker : Install docker-compose plugin.] *****************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *****************************************************************************************
    ok: [host2]
    ok: [host1]

    TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **********************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Configure Docker daemon options.] ***************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **************************************************************************************************
    ok: [host2]
    ok: [host1]

    TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************************************************

    TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************************************************

    RUNNING HANDLER [geerlingguy.docker : restart docker] **********************************************************************************************************************
    changed: [host1]
    changed: [host2]

    TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Get docker group info using getent.] ************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***************************************************************************************
    skipping: [host1]
    skipping: [host2]

    TASK [geerlingguy.docker : include_tasks] **********************************************************************************************************************************
    skipping: [host1]
    skipping: [host2]

    PLAY [Deploy custom docker] ************************************************************************************************************************************************

    TASK [Gathering Facts] *****************************************************************************************************************************************************
    ok: [host2]
    ok: [host1]

    TASK [docker : Install docker] *********************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/docker/tasks/install_docker.yml for host1, host2

    TASK [docker : Install dependencies] ***************************************************************************************************************************************
    ok: [host1]
    ok: [host2]

    TASK [docker : Add apt key] ************************************************************************************************************************************************
    ok: [host1]
    ok: [host2]

    TASK [docker : Add repository] *********************************************************************************************************************************************
    changed: [host2]
    changed: [host1]

    TASK [docker : Install Docker] *********************************************************************************************************************************************
    ok: [host1]
    ok: [host2]

    TASK [docker : Install docker-compose] *************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/docker/tasks/install_compose.yml for host1, host2

    TASK [docker : Install dependencies] ***************************************************************************************************************************************
    changed: [host1]
    changed: [host2]

    TASK [docker : Upgrade pip] ************************************************************************************************************************************************
    changed: [host2]
    changed: [host1]

    TASK [docker : Install docker-compose via pip] *****************************************************************************************************************************
    changed: [host2]
    changed: [host1]

    PLAY RECAP *****************************************************************************************************************************************************************
    host1                      : ok=25   changed=11   unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
    host2                      : ok=25   changed=11   unreachable=0    failed=0    skipped=12   rescued=0    ignored=0

# Inventory outputs

    ansible-inventory -i inventory/inventory --list

    {
        "_meta": {
            "hostvars": {
                "host1": {
                    "ansible_host": "127.0.0.1",
                    "ansible_port": 2222,
                    "ansible_ssh_extra_args": "-o IdentitiesOnly=yes",
                    "ansible_ssh_private_key_file": "./inventory/vagrant/.vagrant/machines/host1/virtualbox/private_key",
                    "ansible_user": "vagrant"
                },
                "host2": {
                    "ansible_host": "127.0.0.1",
                    "ansible_port": 2200,
                    "ansible_ssh_extra_args": "-o IdentitiesOnly=yes",
                    "ansible_ssh_private_key_file": "./inventory/vagrant/.vagrant/machines/host2/virtualbox/private_key",
                    "ansible_user": "vagrant"
                }
            }
        },
        "all": {
            "children": [
                "ungrouped",
                "app"
            ]
        },
        "app": {
            "hosts": [
                "host1",
                "host2"
            ]
        }
    }

# Lab 6 output:

    ansible-playbook ./playbooks/web_app/main.yaml

    PLAY [Ping all hosts] *******************************************************************************************************************************************************************
    TASK [Gathering Facts] ******************************************************************************************************************************************************************
    ok: [localhost]
    TASK [Ping my hosts] ********************************************************************************************************************************************************************
    ok: [localhost]
    PLAY [Deploy web_app python] ************************************************************************************************************************************************************
    TASK [Gathering Facts] ******************************************************************************************************************************************************************
    ok: [localhost]
    TASK [docker : Install docker] **********************************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost
    TASK [docker : Install dependencies] ****************************************************************************************************************************************************
    ok: [localhost]
    TASK [docker : Add apt key] *************************************************************************************************************************************************************
    ok: [localhost]
    TASK [docker : Add repository] **********************************************************************************************************************************************************
    ok: [localhost]
    TASK [docker : Install Docker] **********************************************************************************************************************************************************
    ok: [localhost]
    TASK [docker : Install docker-compose] **************************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost
    TASK [docker : Install dependencies] ****************************************************************************************************************************************************
    ok: [localhost]
    TASK [docker : Upgrade pip] *************************************************************************************************************************************************************
    changed: [localhost]
    TASK [docker : Install docker-compose via pip] *****************************************************************************************************************************************
    ok: [localhost]
    TASK [web_app : Stopping the app] *******************************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/web_app/tasks/0-stop.yml for localhost
    TASK [web_app : Check if Docker Compose directory exists] *******************************************************************************************************************************
    ok: [localhost]
    TASK [web_app : Stop Docker Compose if the directory exists] ****************************************************************************************************************************
    skipping: [localhost]
    TASK [web_app : Wiping containers] ******************************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/web_app/tasks/1-wipe.yml for localhost
    TASK [web_app : Check if directory /app exists] *****************************************************************************************************************************************
    ok: [localhost]
    TASK [web_app : Check if Docker Compose exists] *****************************************************************************************************************************************
    ok: [localhost]
    TASK [web_app : Remove Docker Compose containers if they exist] *************************************************************************************************************************
    changed: [localhost]
    TASK [web_app : Remove Docker Compose files if they exist] ******************************************************************************************************************************
    changed: [localhost]
    TASK [web_app : Remove app directory /app] **********************************************************************************************************************************************
    changed: [localhost]
    TASK [web_app : Deploying the app] ******************************************************************************************************************************************************
    included: /home/jaffart/codes/devops-course-labs/ansible/roles/web_app/tasks/2-deploy.yml for localhost
    TASK [web_app : Create directory for the app container] *********************************************************************************************************************************
    changed: [localhost]
    TASK [web_app : Copy Docker compose] ****************************************************************************************************************************************************
    changed: [localhost]
    TASK [web_app : Copy Docker] ************************************************************************************************************************************************************
    changed: [localhost]
    PLAY RECAP ******************************************************************************************************************************************************************************
    localhost                  : ok=24   changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
