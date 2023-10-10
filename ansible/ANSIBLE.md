# Ansible Best Practices


I applied various best practices while implementing the lab that are listed [here](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html).

## Keep Simple
The project did not require having any complex features of Ansible. This enhances 
readability of the code.

## Naming
I named all playbooks and tasks properly to make the workflow readable.

## Comments
I also provided comments where necessary to make code understandable.

## Dynamic Inventory
I used dynamic inventory using `terraform-inventory` to enhance automation capabilities.

## Separation
All project files are split logically.

## Tasks Blocks
Related tasks are organized within playbooks using Ansible blocks.

## Tagging
Ansible tags are implemented to group tasks logically and enable selective execution.

## Variables
An additional file with default variables is created for **web_app** role.


# Docker Role

I created a custom role for deployment.

## Checking Ansible Setup

```
$ ansible virtualmachines -m ping

vm01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

## Output

```
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Deploy Docker with Ansible role] ******************************************************

TASK [Gathering Facts] **********************************************************************
ok: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Files/Innopolis/Classes/4 year/1 Semester/DevOps/devops-course-labs/ansible/roles/docker/tasks/install_pip.yml for vm01

TASK [docker : Update apt] ******************************************************************
changed: [vm01]

TASK [docker : Install python and pip] ******************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 214 not upgraded.
changed: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Files/Innopolis/Classes/4 year/1 Semester/DevOps/devops-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm01

TASK [docker : Install docker] **************************************************************
changed: [vm01]

TASK [docker : include_tasks] ***************************************************************
included: /mnt/c/Files/Innopolis/Classes/4 year/1 Semester/DevOps/devops-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm01

TASK [docker : Install docker-compose] ******************************************************
changed: [vm01]

PLAY RECAP **********************************************************************************
vm01                       : ok=8    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details

```
$ ansible-inventory -i inventory/inventory.yaml --list

{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_host": "84.23.55.246"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtualmachines"
        ]
    },
    "virtualmachines": {
        "hosts": [
            "vm01"
        ]
    }
}
```

# Dynamic Inventory

In order to implement a dynamic inventory for my project, I used [terraform-inventory](https://github.com/adammck/terraform-inventory).
This tool allows me to retrieve the VM configuration and use it for Ansible.

To use it I created a `dynamic_inventory.sh` bash script which accesses the _.tfstate_ file and passes it further. This file is based on the solution from [this discussion](https://github.com/adammck/terraform-inventory/issues/121).

Another possible way to use it is to cd to _terraform/vkcloud_ folder first:

`cd terraform/vkcloud`

And then, run the following command and provide the full path to _terraform-inventory_ executable:

`ansible-playbook --inventory-file="path to exe of terraform inventory" "../../playbooks/dev/main.yaml"`

The result of the execution is pretty the same as the one from output above.


# Web Application Deployment using Docker compose

**Python:**

```
$ ansible-playbook playbooks/dev/app_python/main.yaml --diff

PLAY [Deploy python docker app with Ansible role] *********************************************

TASK [Gathering Facts] ************************************************************************
ok: [vm01]

TASK [docker : Update apt] ********************************************************************
changed: [vm01]

TASK [docker : Install python and pip] ********************************************************
ok: [vm01]

TASK [docker : Update cache] ******************************************************************
changed: [vm01]

TASK [docker : Install dependencies] **********************************************************
ok: [vm01]

TASK [docker : Add apt key] *******************************************************************
changed: [vm01]

TASK [docker : Add repository] ****************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [vm01]

TASK [docker : Install Docker] ****************************************************************
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  libltdl7 pigz docker-buildx-plugin docker-compose-plugin slirp4netns
The following NEW packages will be installed:
  containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras
0 upgraded, 4 newly installed, 0 to remove and 104 not upgraded.
changed: [vm01]

TASK [docker : Install docker-compose] ********************************************************
ok: [vm01]

TASK [web_app : Check if docker-compose file exists] ******************************************
ok: [vm01]

TASK [web_app : Check if web app directory exists] ********************************************
ok: [vm01]

TASK [web_app : Remove docker containers] *****************************************************
changed: [vm01]

TASK [web_app : Delete web application directory] *********************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/app_python",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/app_python/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [vm01]

TASK [web_app : Create directory for the app] *************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [vm01]

TASK [web_app : Create docker-compose file] ***************************************************
--- before
+++ after: /home/vladimir_ka/.ansible/tmp/ansible-local-859na3m65bb/tmpmyg4k3gu/docker-compose.yml.j2
@@ -0,0 +1,9 @@
+version: '3.9'
+
+services:
+  web_app_python:
+    image: vladimirka002/innopolis-devops-python-app
+    container_name: innopolis-devops-python-app
+    ports:
+      - 5000:8000
+    restart: always
\ No newline at end of file

changed: [vm01]

RUNNING HANDLER [web_app : Run Docker Compose] ************************************************
changed: [vm01]

PLAY RECAP ************************************************************************************
vm01                       : ok=16   changed=10   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```