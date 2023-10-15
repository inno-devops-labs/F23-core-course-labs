# Ansible.md

## Ansible for Docker

### The output of ` ansible-playbook ansible/playbooks/dev/main.yaml -i ansible/inventory/default.yaml`

``` bash
    PLAY [yandex_instance] ***************************************************************************************************************************

    TASK [Gathering Facts] ***************************************************************************************************************************
    The authenticity of host '130.193.41.195 (130.193.41.195)' can't be established.
    ED25519 key fingerprint is SHA256:O9PqhOCF6jmdI/7To/cHwRQmTWrNMUsPxWHco6Ry3Fw.
    This key is not known by any other names
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    ok: [yandex_instance]

    TASK [geerlingguy.docker : Load OS-specific vars.] ***********************************************************************************************
    ok: [yandex_instance]

    TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************
    included: /home/khays/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for yandex_instance

    TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *********************************************************************
    ok: [yandex_instance]

    TASK [geerlingguy.docker : Ensure dependencies are installed.] ***********************************************************************************
    changed: [yandex_instance]

    TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ******************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***************************************************
    ok: [yandex_instance]

    TASK [geerlingguy.docker : Add Docker apt key.] **************************************************************************************************
    changed: [yandex_instance]

    TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ******************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Add Docker repository.] ***********************************************************************************************
    changed: [yandex_instance]

    TASK [geerlingguy.docker : Install Docker packages.] *********************************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *********************************************************************
    changed: [yandex_instance]

    TASK [geerlingguy.docker : Install docker-compose plugin.] ***************************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***************************************************************
    ok: [yandex_instance]

    TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ********************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Configure Docker daemon options.] *************************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ************************************************************************
    ok: [yandex_instance]

    TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ********************************************************

    RUNNING HANDLER [geerlingguy.docker : restart docker] ********************************************************************************************
    changed: [yandex_instance]

    TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Get docker group info using getent.] **********************************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *************************************************************
    skipping: [yandex_instance]

    TASK [geerlingguy.docker : include_tasks] ********************************************************************************************************
    skipping: [yandex_instance]

    PLAY RECAP ***************************************************************************************************************************************
    yandex_instance            : ok=12   changed=5    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0  
```

## Custom Docker Role

``` bash
    PLAY [Install docker and docker compose [custom-role]] *******************************************************************************************

    TASK [Gathering Facts] ***************************************************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include update_apt] ***************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/update_apt.yml for yandex_instance

    TASK [../../roles/docker : Update and upgrade apt packages] **************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include install_pip] **************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for yandex_instance

    TASK [../../roles/docker : Install python3 and pip] **********************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include install_docker] ***********************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_instance

    TASK [../../roles/docker : Remove conflicting package containerd.io] *****************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Install Docker using apt] *********************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include install_compose] **********************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_instance

    TASK [../../roles/docker : Install Docker Compose using pip] *************************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/docker : Include check_install] ************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/check_install.yml for yandex_instance

    TASK [../../roles/docker : Check if Docker is installed] *****************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Check if Docker Compose is installed] *********************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/docker : Print Docker installation status] *************************************************************************************
    ok: [yandex_instance] => {
        "msg": "Docker is installed"
    }

    TASK [../../roles/docker : Print Docker Compose installation status] *****************************************************************************
    ok: [yandex_instance] => {
        "msg": "Docker Compose is installed"
    }

    PLAY RECAP ***************************************************************************************************************************************
    yandex_instance            : ok=15   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Inventory

``` bash
{
    "_meta": {
        "hostvars": {
            "yandex_instance": {
                "ansible_ssh_host": "130.193.41.195",
                "ansible_ssh_private_key_file": "../authorized_key.json",
                "ansible_user": "admin"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_cloud"
        ]
    },
    "yandex_cloud": {
        "hosts": [
            "yandex_instance"
        ]
    }
}
```

### Ansible Inventory Explanation

The JSON inventory file defines how Ansible connects to hosts and organizes them into groups. Here's a breakdown of the inventory structure:

1. **\_meta**: Contains host-specific metadata, including connection details for the `yandex_instance` host.

    - `ansible_ssh_host`: IP address or hostname.
    - `ansible_ssh_private_key_file`: Path to the SSH key.
    - `ansible_user`: SSH username.

2. **all**: A group that encompasses all hosts in the inventory. It includes two subgroups:

    - `ungrouped`: Empty group for hosts with no specific group.
    - `yandex_cloud`: Group containing the `yandex_instance` host.

3. **yandex_cloud**: Group with hosts (e.g., `yandex_instance`).

## Output from web_app

```bash
    PLAY [Install docker and docker compose [custom-role]] *******************************************************************************************

    TASK [Gathering Facts] ***************************************************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include update_apt] ***************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/update_apt.yml for yandex_instance

    TASK [../../roles/docker : Update and upgrade apt packages] **************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include install_pip] **************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for yandex_instance

    TASK [../../roles/docker : Install python3 and pip] **********************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include install_docker] ***********************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_instance

    TASK [../../roles/docker : Remove conflicting package containerd.io] *****************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Install Docker using apt] *********************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include install_compose] **********************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_instance

    TASK [../../roles/docker : Install Docker Compose using pip] *************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Include check_install] ************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/docker/tasks/check_install.yml for yandex_instance

    TASK [../../roles/docker : Check if Docker is installed] *****************************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/docker : Check if Docker Compose is installed] *********************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/docker : Print Docker installation status] *************************************************************************************
    ok: [yandex_instance] => {
        "msg": "Docker is installed"
    }

    TASK [../../roles/docker : Print Docker Compose installation status] *****************************************************************************
    ok: [yandex_instance] => {
        "msg": "Docker Compose is installed"
    }

    TASK [../../roles/web_app : Include wipe_containers] *********************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/web_app/tasks/wipe_containers.yml for yandex_instance

    TASK [../../roles/web_app : Stop container] ******************************************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/web_app : Delete container] ****************************************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/web_app : Delete image] ********************************************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/web_app : Move docker-compose to the target] ***********************************************************************************
    ok: [yandex_instance]

    TASK [../../roles/web_app : Include build_docker] ************************************************************************************************
    included: /home/khays/DevOps/core-course-labs/ansible/roles/web_app/tasks/build_docker.yml for yandex_instance

    TASK [../../roles/web_app : Pull docker image from docker hub] ***********************************************************************************
    changed: [yandex_instance]

    TASK [../../roles/web_app : Deploy docker container] *********************************************************************************************
    changed: [yandex_instance]

    PLAY RECAP ***************************************************************************************************************************************
    yandex_instance            : ok=23   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```
