# Usage
```
ansible-playbook playbooks/dev/main.yaml --diff --private-key=~/.ssh/id_ed25519
ansible-playbook playbooks/dev/app_python/main.yml --diff --private-key=~/.ssh/id_ed25519
ansible-playbook playbooks/dev/app_python/main.yml --diff --private-key=~/.ssh/id_ed25519 --extra-vars "web_app_full_wipe=1" --tags wipe
ansible-playbook playbooks/dev/app_bash/main.yml --diff --private-key=~/.ssh/id_ed25519
ansible-playbook playbooks/dev/app_bash/main.yml --diff --private-key=~/.ssh/id_ed25519 --extra-vars "web_app_full_wipe=1" --tags wipe
```
yandex dynamic inventory:
```
ansible-inventory --list
```

# Deployment Output
```
PLAY [Deploy docker] ****************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install pip] *********************************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for terraform1

TASK [docker : Update apt] **********************************************************************************************************************************************************************************************************
changed: [terraform1]

TASK [docker : Install python] ******************************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install pip] *********************************************************************************************************************************************************************************************************
The following additional packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
  libbinutils libc-dev-bin libc6 libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
  libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-9-dev libgdbm-compat4 libgomp1 libisl22 libitm1 liblsan0 libmpc3
  libmpfr6 libperl5.30 libpython3-dev libpython3.8-dev libquadmath0
  libstdc++-9-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev patch
  perl perl-modules-5.30 python-pip-whl python3-dev python3-wheel
  python3.8-dev zlib1g-dev
Suggested packages:
  binutils-doc cpp-doc gcc-9-locales debian-keyring g++-multilib
  g++-9-multilib gcc-9-doc gcc-multilib autoconf automake libtool flex bison
  gdb gcc-doc gcc-9-multilib glibc-doc git bzr libstdc++-9-doc make-doc
  diffutils-doc perl-doc libterm-readline-gnu-perl
  | libterm-readline-perl-perl libb-debug-perl liblocale-codes-perl
The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
  libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
  libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-9-dev libgdbm-compat4 libgomp1 libisl22 libitm1 liblsan0 libmpc3
  libmpfr6 libperl5.30 libpython3-dev libpython3.8-dev libquadmath0
  libstdc++-9-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev patch
  perl perl-modules-5.30 python-pip-whl python3-dev python3-pip python3-wheel
  python3.8-dev zlib1g-dev
The following packages will be upgraded:
  libc6
1 upgraded, 56 newly installed, 0 to remove and 4 not upgraded.
changed: [terraform1]

TASK [docker : Install docker] ******************************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install docker] ******************************************************************************************************************************************************************************************************
changed: [terraform1]

TASK [docker : Install docker-compose] **********************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose via pip] **************************************************************************************************************************************************************************************
changed: [terraform1]

PLAY RECAP **************************************************************************************************************************************************************************************************************************
terraform1                 : ok=9    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

# Inventory Details
```
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "158.160.109.240"
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

# app_python deployment output(web_app role)
```
TASK [docker : Install docker] ************************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Update apt and install docker-ce] ******************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker Module for Python] ******************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install docker-compose] ****************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose via pip] ********************************************************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Install application] ******************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/web_app/tasks/install.yml for terraform1

TASK [web_app : Create a directory if it does not exist] **********************************************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/zrrrget/app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Create docker-compose] ****************************************************************************************************************************************************************************************
--- before
+++ after: /home/zrrrget/.ansible/tmp/ansible-local-3620164k_mc068/tmpi5nd35wz/docker-compose.yml.j2
@@ -0,0 +1,6 @@
+version: "3.7"
+services:
+  app:
+    image: zrrrget/app_python
+    ports:
+      - "8000:8000"

changed: [terraform1]

TASK [web_app : Run application] **********************************************************************************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Wipe appliction] **********************************************************************************************************************************************************************************************
skipping: [terraform1]

PLAY RECAP ********************************************************************************************************************************************************************************************************************
terraform1                 : ok=16   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```
# app_bash output
```
TASK [docker : Install pip] *******************************************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install docker] ****************************************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Add Docker GPG apt Key] ********************************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker Repository] *********************************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Update apt and install docker-ce] **********************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker Module for Python] **********************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install docker-compose] ********************************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose via pip] ************************************************************************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Install application] **********************************************************************************************************************************************************************************************************
included: /home/zrrrget/projects/core-course-labs/ansible/roles/web_app/tasks/install.yml for terraform1

TASK [web_app : Create a directory if it does not exist] **************************************************************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/zrrrget/app_bash",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Create docker-compose] ********************************************************************************************************************************************************************************************************
--- before
+++ after: /home/zrrrget/.ansible/tmp/ansible-local-3549671gjkg096/tmp83kq409v/docker-compose.yml.j2
@@ -0,0 +1,6 @@
+version: "3.7"
+services:
+  app:
+    image: zrrrget/app_bash
+    ports:
+      - "8000:8000"

changed: [terraform1]

TASK [web_app : Run application] **************************************************************************************************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Wipe appliction] **************************************************************************************************************************************************************************************************************
skipping: [terraform1]

PLAY RECAP ************************************************************************************************************************************************************************************************************************************
terraform1                 : ok=16   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```