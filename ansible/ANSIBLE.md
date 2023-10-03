# Best practices:

- Generous use of whitespace (simple to read)
- Using of namings (Ansible shows you the name of each named entity it runs)
- Mention the state
- Use comments
- Use dynamic inventory with clouds

ansible-playbook ansible/playbooks/dev/main.yaml --diff
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

 ansible-playbook --ask-become-pass  ansible/playbooks/dev/main.yaml --diff
BECOME password: 
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Dev] *****************************************************************************************************************************************************************************************************************************

TASK [docker : include_tasks] **********************************************************************************************************************************************************************************************************
included: /home/irina/PycharmProjects/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for localhost

TASK [docker : Install pip] ************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] **********************************************************************************************************************************************************************************************************
included: /home/irina/PycharmProjects/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install Docker packages.] ***********************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Install docker-compose plugin.] *****************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Ensure /etc/docker/ directory exists.] **********************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Configure Docker daemon options.] ***************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Ensure Docker is started and enabled at boot.] **************************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] **********************************************************************************************************************************************************

TASK [docker : include_tasks] **********************************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Get docker group info using getent.] ************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Check if there are any users to add to the docker group.] ***************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : include_tasks] **********************************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : include_tasks] **********************************************************************************************************************************************************************************************************
included: /home/irina/PycharmProjects/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Check current docker-compose version.] **********************************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : set_fact] ***************************************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Delete existing docker-compose version if it's different.] **************************************************************************************************************************************************************
skipping: [localhost]

TASK [docker : Install Docker Compose] *************************************************************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP *****************************************************************************************************************************************************************************************************************************
localhost                  : ok=7    changed=1    unreachable=0    failed=0    skipped=10   rescued=0    ignored=0   



ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
[WARNING]:  * Failed to parse /home/irina/PycharmProjects/core-course-labs/ansible/inventory/default_aws_ec2.yml with auto plugin: inventory config '/home/irina/PycharmProjects/core-course-
labs/ansible/inventory/default_aws_ec2.yml' specifies unknown plugin 'yacloud_compute'
[WARNING]:  * Failed to parse /home/irina/PycharmProjects/core-course-labs/ansible/inventory/default_aws_ec2.yml with yaml plugin: Plugin configuration YAML file, not YAML inventory
[WARNING]:  * Failed to parse /home/irina/PycharmProjects/core-course-labs/ansible/inventory/default_aws_ec2.yml with ini plugin: Invalid host pattern 'plugin:' supplied, ending in ':' is not allowed, this character is reserved to
provide a port.
[WARNING]: Unable to parse /home/irina/PycharmProjects/core-course-labs/ansible/inventory/default_aws_ec2.yml as an inventory source
[WARNING]: No inventory was parsed, only implicit localhost is available
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}

