# Last 50 lines of the output:

```diff
changed: [vm-app-python]

TASK [docker : Add Docker Repository] ******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu focal stable

changed: [vm-app-python]

TASK [docker : Update apt and install docker-ce] *******************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin git git-man libcurl3-gnutls liberror-perl pigz
  slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite git-daemon-run | git-daemon-sysvinit
  git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin git git-man libcurl3-gnutls
  liberror-perl pigz slirp4netns
0 upgraded, 12 newly installed, 0 to remove and 29 not upgraded.
changed: [vm-app-python]

TASK [docker : ansible.builtin.include_tasks] **********************************
included: /Users/arina/projects/core-course-labs/ansible/roles/docker/tasks/install_pip_package.yaml for vm-app-python

TASK [docker : Install Docker Module for Python] *******************************
changed: [vm-app-python]

TASK [Pull default Docker image] ***********************************************
changed: [vm-app-python]

TASK [Create container] ********************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [vm-app-python]

PLAY RECAP *********************************************************************
vm-app-python              : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

# Inventory:

```json
{
  "_meta": {
    "hostvars": {
      "vm-app-python": {
        "ansible_host": "51.250.75.123",
        "ansible_user": "ansible"
      }
    }
  },
  "all": { "children": ["ungrouped", "yandex"] },
  "yandex": { "hosts": ["vm-app-python"] }
}
```

For generation of inventory i used terraform `local_file` with `templatefile`, so inventory resources are synced with terraform state.
