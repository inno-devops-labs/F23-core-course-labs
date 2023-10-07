# Ansible

## Install Docker to Virtual Machines

1. **Create ssh on Host machine**:

    We are going to connect to our VMs via ssh, so we need to create new ssh key on our Host machine:
    ```shell
    ssh-keygen -t ed25519
    ```

1. **Connect to your VMs and set up new user**:

    Connect to VM using GUI, ssh, or any other tool.
    Create new user and add ssh public key to that VM for created user.
    Open terminal and put the following instructions:
    ```shell
    sudo useradd -m -d /home/yesliesnayder -s /bin/bash yesliesnayder
    sudo su - yesliesnayder
    mkdir .ssh
    touch .ssh/authorized_keys
    echo "<public_key>" > /home/testuser/.ssh/authorized_keys
    chmod 700 ~/.ssh
    chmod 600 ~/.ssh/authorized_keys
    ```
    
    Instead of `yesliesnayder` write your username to connect and 
    `<public_key>` should be from your ssh file that you created on Host machine.

1. **Check connection**:

    ```shell
    ansible virtual_machines -m ping -i inventory/default_local.yml
    ```
   Make sure that in `inventory/default_local.yml` file you have metagroup called `virtual_machines`,
   and check IP addresses of your VMs.

   Output:
    ```text
    vm-1 | SUCCESS => {
        "ansible_facts": {
            "discovered_interpreter_python": "/usr/bin/python3"
        },
        "changed": false,
        "ping": "pong"
    }
    ```
   
1. **Deploy Docker**:

    Beforehand, install Docker role: `ansible-galaxy install geerlingguy.docker`.
    Launch the playbook to deploy Docker and Docker Compose to you VMs:

    ```shell
    ansible-playbook -i inventory/default_local.yml playbooks/dev/main.yaml
    ```
   
    Output:
    ```text
    ...
    TASK [geerlingguy.docker : Add Docker apt key.] ********************************************************************
    ok: [vm-1]
    
    TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *********************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Add Docker repository.] *****************************************************************
    changed: [vm-1]
    
    TASK [geerlingguy.docker : Install Docker packages.] ***************************************************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***************************************
    ok: [vm-1]
    
    TASK [geerlingguy.docker : Install docker-compose plugin.] *********************************************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *********************************
    ok: [vm-1]
    
    TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************************************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Configure Docker daemon options.] *******************************************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******************************************
    ok: [vm-1]
    
    TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **************************
    
    TASK [geerlingguy.docker : include_tasks] **************************************************************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Get docker group info using getent.] ****************************************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *******************************
    skipping: [vm-1]
    
    TASK [geerlingguy.docker : include_tasks] **************************************************************************
    skipping: [vm-1]
    
    PLAY RECAP *********************************************************************************************************
    vm-1                       : ok=11   changed=1    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0 
    ```
   
1. **Inventory Details**:

    Let's check information about your inventory:
    ```shell
    ansible-inventory -i inventory/default_local.yml --list
    ```
   
    Output:
    ```text
    {
        "_meta": {
            "hostvars": {
                "vm-1": {
                    "ansible_host": "172.16.49.128",
                    "ansible_user": "yesliesnayder"
                }
            }
        },
        "all": {
            "children": [
                "ungrouped",
                "virtual_machines"
            ]
        },
        "virtual_machines": {
            "hosts": [
                "vm-1"
            ]
        }
    }
    ```

## Dynamic inventory

1. Make sure, you put `yacloud_compute.py` file in ansible plugins

1. Check if dynamic inventory works:

   ```shell
   ansible-inventory -i inventory/yacloud_compute.yml --graph
   ```
   
   Output:
   ```text
   @all:
     |--@ungrouped:
     |--@yacloud:
     |  |--my-vm-2
     |  |--my-vm-1
   ```
   
   If you have problems with it, check if this command contains path to plugin `yacloud_compute.py`:
   ```shell
   ansible-config dump | grep DEFAULT_INVENTORY_PLUGIN_PATH
   ```
   If output doesn't contain path to the plugin then put this plugin into one of the paths in output.

1. To use dynamic inventory for yandex cloud, use the following command:

   ```shell
   ansible-playbook -i inventory/yacloud_compute.yml playbooks/dev/main.yaml
   ```