# Ansible

## Lab 5
## Docker role

### Command:
```
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml --diff
```
### Output:
```
TASK [../../roles/docker : Ensure curl is present (on older systems without SNI).] ***
ok: [vm01]

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm01

TASK [../../roles/docker : Add Docker apt key.] ********************************
ok: [vm01]

TASK [../../roles/docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [vm01]

TASK [../../roles/docker : Add Docker repository.] *****************************
ok: [vm01]

TASK [../../roles/docker : Install Docker packages.] ***************************
skipping: [vm01]

TASK [../../roles/docker : Install Docker packages (with downgrade option).] ***
ok: [vm01]

TASK [../../roles/docker : Ensure Docker is started and enabled at boot.] ******
ok: [vm01]

TASK [../../roles/docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm01

TASK [../../roles/docker : Check current docker-compose version.] **************
ok: [vm01]

TASK [../../roles/docker : set_fact] *******************************************
ok: [vm01]

TASK [../../roles/docker : Delete existing docker-compose version if it's different.] ***
skipping: [vm01]

TASK [../../roles/docker : Install Docker Compose (if configured).] ************
skipping: [vm01]

TASK [../../roles/docker : Get docker group info using getent.] ****************
skipping: [vm01]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] ***
skipping: [vm01]

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ********

PLAY RECAP *********************************************************************
vm01                       : ok=13   changed=0    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0 
```
### Command:
```
ansible-inventory -i default_aws_ec2.yml --list 
```

### Output:

```
{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_host": "158.160.107.44",
                "ansible_user": "ubuntu"
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
            "vm01"
        ]
    }
}
```

## Dynamic inventory 
I've used inventory plugin for Yandex Cloud proposed in the task.
###  Command:
```
ansible-playbook playbooks/dev/main.yaml --diff 
```
### Output:
```
TASK [../../roles/docker : Ensure curl is present (on older systems without SNI).] ***
ok: [terraform1]

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [../../roles/docker : Add Docker apt key.] ********************************
ok: [terraform1]

TASK [../../roles/docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [terraform1]

TASK [../../roles/docker : Add Docker repository.] *****************************
ok: [terraform1]

TASK [../../roles/docker : Install Docker packages.] ***************************
skipping: [terraform1]

TASK [../../roles/docker : Install Docker packages (with downgrade option).] ***
ok: [terraform1]

TASK [../../roles/docker : Ensure Docker is started and enabled at boot.] ******
ok: [terraform1]

TASK [../../roles/docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [../../roles/docker : include_tasks] **************************************
included: /Users/alinasafina/DevOps-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [../../roles/docker : Check current docker-compose version.] **************
ok: [terraform1]

TASK [../../roles/docker : set_fact] *******************************************
ok: [terraform1]

TASK [../../roles/docker : Delete existing docker-compose version if it's different.] ***
skipping: [terraform1]

TASK [../../roles/docker : Install Docker Compose (if configured).] ************
skipping: [terraform1]

TASK [../../roles/docker : Get docker group info using getent.] ****************
skipping: [terraform1]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] ***
skipping: [terraform1]

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ********

PLAY RECAP *********************************************************************
terraform1                 : ok=13   changed=0    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   
```

### Command:
```
ansible-inventory -i inventory/yacloud_compute.yml --list  
```

### Output:
```
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "158.160.107.44"
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
            "terraform1"
        ]
    }
}

```

terraform1 - name of my VM in YandexCLoud, so dynamic host resolution works.

## Lab 6
## app_python:
### Command: 
```
ansible-playbook playbooks/dev/app_python/main.yaml --diff
```
### Output (web_app_full_wipe: false)

```
TASK [web_app : Create dir for app_python] *********************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Create directory for docker compose] ***********************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_python/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Run docker compose] ****************************************************************************************************************************************
--- before
+++ after: /Users/alinasafina/.ansible/tmp/ansible-local-28473_g81e5rm/tmp1vbdf62n/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  app_python:
+    image: "lnsfna/app_python:latest"
+    container_name: "app_python"
+    ports:
+      - "8080:8080"
+    restart: unless-stopped

changed: [terraform1]

TASK [web_app : Check if directory /app_python exists] *********************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Check if docker compose exists] ****************************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove containers if exists] *******************************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove docker compose file if exists] **********************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove app directory /app_python] **************************************************************************************************************************
skipping: [terraform1]

RUNNING HANDLER [web_app : Restart docker compose] *************************************************************************************************************************
changed: [terraform1]

PLAY RECAP *****************************************************************************************************************************************************************
terraform1                 : ok=17   changed=4    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0 
```
### Output (web_app_full_wipe: true)
```
TASK [web_app : Create directory for docker compose] ***********************************************************************************************************************
ok: [terraform1]

TASK [web_app : Run docker compose] ****************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Check if directory /app_python exists] *********************************************************************************************************************
ok: [terraform1]

TASK [web_app : Check if docker compose exists] ****************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Remove containers if exists] *******************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Remove docker compose file if exists] **********************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/app_python/docker-compose",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/app_python/docker-compose/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform1]

TASK [web_app : Remove app directory /app_python] **************************************************************************************************************************
--- before
+++ after
@@ -1,8 +1,4 @@
 {
     "path": "/app_python",
-    "path_content": {
-        "directories": [],
-        "files": []
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform1]

PLAY RECAP *****************************************************************************************************************************************************************
terraform1                 : ok=21   changed=3    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0   
```

## app_go:
### Command: 
```
ansible-playbook playbooks/dev/app_go/main.yaml --diff
``` 

### Output (web_app_full_wipe: false)
```
TASK [web_app : Create dir for app_go] *************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_go",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Create directory for docker compose] ***********************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/app_go/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Run docker compose] ****************************************************************************************************************************************
--- before
+++ after: /Users/alinasafina/.ansible/tmp/ansible-local-29712gcv9sotx/tmpume4eovc/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  app_go:
+    image: "lnsfna/app_go:latest"
+    container_name: "app_go"
+    ports:
+      - "8081:8081"
+    restart: unless-stopped

changed: [terraform1]

TASK [web_app : Check if directory /app_go exists] *************************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Check if docker compose exists] ****************************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove containers if exists] *******************************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove docker compose file if exists] **********************************************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove app directory /app_go] ******************************************************************************************************************************
skipping: [terraform1]

RUNNING HANDLER [web_app : Restart docker compose] *************************************************************************************************************************
changed: [terraform1]

PLAY RECAP *****************************************************************************************************************************************************************
terraform1                 : ok=17   changed=4    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0  
```
### Output (web_app_full_wipe: true)
```
ansible-playbook playbooks/dev/app_go/main.yaml --diff
```

```
TASK [web_app : Create directory for docker compose] ***********************************************************************************************************************
ok: [terraform1]

TASK [web_app : Run docker compose] ****************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Check if directory /app_go exists] *************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Check if docker compose exists] ****************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Remove containers if exists] *******************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Remove docker compose file if exists] **********************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/app_go/docker-compose",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/app_go/docker-compose/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform1]

TASK [web_app : Remove app directory /app_go] ******************************************************************************************************************************
--- before
+++ after
@@ -1,8 +1,4 @@
 {
     "path": "/app_go",
-    "path_content": {
-        "directories": [],
-        "files": []
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform1]

PLAY RECAP *****************************************************************************************************************************************************************
terraform1                 : ok=21   changed=3    unreachable=0    failed=0    skipped=6    rescued=0    ignored=0 
```