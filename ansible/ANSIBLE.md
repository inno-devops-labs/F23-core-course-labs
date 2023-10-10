# Ansible-related work

## Lab 5

### Deployment

```zsh
$ ansible-playbook playbooks/dev/main.yaml --diff
...

TASK [roles/docker : include_tasks] ************************************************************************************
included: /Users/dinar/devops-course/ansible/roles/docker/tasks/install_pip.yml for localhost

TASK [roles/docker : Install pip] **************************************************************************************
ok: [localhost]

TASK [roles/docker : include_tasks] ************************************************************************************
included: /Users/dinar/devops-course/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [roles/docker : Update apt cache] *********************************************************************************
ok: [localhost]

TASK [roles/docker : Install Docker dependencies] **********************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 48 not upgraded.
changed: [localhost]

TASK [roles/docker : Add Docker apt key] *******************************************************************************
changed: [localhost]

TASK [roles/docker : Add Docker repository] ****************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [localhost]

TASK [roles/docker : Install Docker] ***********************************************************************************
The following additional packages will be installed:
  dbus-user-session docker-buildx-plugin docker-compose-plugin libltdl7
  libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io dbus-user-session docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 11 newly installed, 0 to remove and 48 not upgraded.
changed: [localhost]

TASK [roles/docker : include_tasks] ************************************************************************************
included: /Users/dinar/devops-course/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [roles/docker : Install Docker Compose] ***************************************************************************
changed: [localhost]

PLAY RECAP *************************************************************************************************************
localhost                  : ok=11   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory 

```zsh
$ ansible-inventory -i inventory/inventory_local.yml --list
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "devhost"
        ]
    },
    "devhost": {
        "hosts": [
            "localhost"
        ]
    }
}
```

## Lab 6

```zsh
$ ansible-playbook playbooks/dev/main.yaml --diff
 
PLAY [Deploy docker image] *********************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [localhost]

TASK [web_app : Check if container exists] *****************************************************************************
ok: [localhost]

TASK [web_app : Stop the container if it exists] ***********************************************************************
skipping: [localhost]

TASK [web_app : Remove the container if it exists] *********************************************************************
skipping: [localhost]

TASK [web_app : Pull the Docker image] *********************************************************************************
ok: [localhost]

TASK [web_app : Run the Docker container] ******************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [localhost]

PLAY RECAP *************************************************************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

### Role structure

```
.
|-- defaults
|   `-- main.yml
|-- meta
|   `-- main.yml
|-- tasks
|   |-- wipe_app.yml
|   |-- stop_app.yml
|   |-- deploy_app.yml
|   `-- main.yml
`-- templates
    `-- docker-compose.yml.j2
```

There are two new tasks: `stop_app` and `deploy_app`.


- `stop_app` task stops container when there are no need to use wipe
- `deploy_app` task deploys docker compose

### Outputs

```zsh
$ ansible-playbook playbooks/dev/main.yaml --diff
TASK [web_app : Create directory for my-app] *********************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/my-app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Create directory for Docker Compose] *************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/my-app/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Run Docker Compose by template] ******************************************************************************************
--- before
+++ after: /root/.ansible/tmp/ansible-local-11072cnw01ff9/tmplfypnnrh/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  my-app:
+    image: "dshamik/moscow-time-flask-app:latest"
+    container_name: "my-container"
+    ports:
+      - "8090:8090"
+    restart: unless-stopped
\ No newline at end of file

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker Compose] ***************************************************************************************
changed: [localhost]

PLAY RECAP *******************************************************************************************************************************
localhost                  : ok=21   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```



