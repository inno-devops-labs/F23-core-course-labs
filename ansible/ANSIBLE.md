# Ansible

## Last 50 lines

```
PLAY [Prepare docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [vk-cloud]

TASK [docker : include_tasks] **************************************************
included: /home/omp.ru/i.petrov/Documents/User/DevOpsLabs/ansible/roles/docker/tasks/install_docker.yml for vk-cloud

TASK [docker : Install pip] ****************************************************
The following additional packages will be installed:
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
  manpages-dev python3-dev python3-wheel python3.10-dev rpcsvc-proto
  zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc
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
changed: [vk-cloud]

TASK [docker : Install Docker using pip] ***************************************
changed: [vk-cloud]

TASK [docker : include_tasks] **************************************************
included: /home/omp.ru/i.petrov/Documents/User/DevOpsLabs/ansible/roles/docker/tasks/install_compose.yml for vk-cloud

TASK [docker : Install Docker Compose] *****************************************
changed: [vk-cloud]

TASK [web_app : Add app path] **************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/web_app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [vk-cloud]

TASK [web_app : Add docker-compose] ********************************************
--- before
+++ after: /home/omp.ru/i.petrov/.ansible/tmp/ansible-local-18423dnwbxspc/tmp72ogiv8k/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+services:
+  web_app:
+    hostname: web_app
+    image: ign19ht/dev-ops-labs:latest
+    restart: always
+    ports:
+      - "8000:8000"
+    command: "python3 main.py"

changed: [vk-cloud]

TASK [web_app : Run docker-compose] ********************************************
changed: [vk-cloud]

PLAY RECAP *********************************************************************
vk-cloud                   : ok=9    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
