
## Ansible setup

I installed and set up ansible to manage one vm host.

The vm host and user name is specified in `inventory` directory.

### Checking the setup:
```
r-shakirova-osx:ansible r-shakirova$ ansible all --list-hosts -i inventory
  hosts (1):
    virtual_machine_1
r-shakirova-osx:ansible r-shakirova$ ansible all -m ping -i inventory
virtual_machine_1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

### Inventory details:
```
r-shakirova-osx:ansible r-shakirova$ ansible-inventory -i inventory --list
{
    "_meta": {
        "hostvars": {
            "virtual_machine_1": {
                "ansible_host": "51.250.14.244",
                "ansible_ssh_user": "vm-admin"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vms"
        ]
    },
    "vms": {
        "hosts": [
            "virtual_machine_1"
        ]
    }
}
```

## Custom Docker Role
Custom docker role for installing docker and docker-compose using pip on my vm.

The role is executed via `playbooks/docker/main.yml`

The output of the role's execution is the following:
```
r-shakirova-osx:ansible r-shakirova$ ansible-playbook playbooks/docker/main.yml -i inventory/default.yml --diff

PLAY [Deploy Docker with Ansible role] ***************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
ok: [virtual_machine_1]

TASK [docker : Install pip] **************************************************************************************************************************************
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 0 not upgraded.
changed: [virtual_machine_1]

TASK [docker : Update pip] ***************************************************************************************************************************************
changed: [virtual_machine_1]

TASK [docker : include_tasks] ************************************************************************************************************************************
included: /Users/r-shakirova/DEVOPS/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for virtual_machine_1

TASK [docker : Docker packages] **********************************************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 6 not upgraded.
changed: [virtual_machine_1]

TASK [docker : Doceker repository] *******************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=x86_64] https://download.docker.com/linux/ubuntu focal stable

changed: [virtual_machine_1]

TASK [docker : Docker python module] *****************************************************************************************************************************
changed: [virtual_machine_1]

TASK [docker : include_tasks] ************************************************************************************************************************************
included: /Users/r-shakirova/DEVOPS/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for virtual_machine_1

TASK [docker : Install docker-compose] ***************************************************************************************************************************
changed: [virtual_machine_1]

PLAY RECAP *******************************************************************************************************************************************************
virtual_machine_1          : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Web_app role
I created a role that deploys and runs a spercified docker image.
The last lines of deployment command:

```
TASK [web_app : Stop app] ****************************************************************************************************************************************
changed: [virtual_machine_1]

TASK [web_app : delete image] ************************************************************************************************************************************
changed: [virtual_machine_1]

TASK [web_app : Remove compose directory] ************************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/opt/composes/rentacat45/python-web-app",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/opt/composes/rentacat45/python-web-app/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [virtual_machine_1]

TASK [web_app : Create a directory if it does not exist] *********************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/composes/rentacat45/python-web-app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [virtual_machine_1]

TASK [web_app : Create docker-compose] ***************************************************************************************************************************
--- before
+++ after: /Users/r-shakirova/.ansible/tmp/ansible-local-17830w0btclym/tmp7m8ia74f/docker-compose.yml.j2
@@ -0,0 +1,4 @@
+version: "3"
+services:
+  app:
+    image: rentacat45/python-web-app

changed: [virtual_machine_1]

TASK [web_app : Run application] *********************************************************************************************************************************
changed: [virtual_machine_1]

PLAY RECAP *******************************************************************************************************************************************************
virtual_machine_1          : ok=15   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```