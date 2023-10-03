# Docker role

Latest 50 lines of plybook which just installs Docker

```
dyllas@DyllasDekWork:/mnt/d/git/core-course-labs/ansible$ ansible-playbook main.yaml -i ./inventory/inv.yaml --diff
[WARNING]: Ansible is being run in a world writable directory (/mnt/d/git/core-course-labs/ansible),
ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
[DEPRECATION WARNING]: "include" is deprecated, use include_tasks/import_tasks instead. See
https://docs.ansible.com/ansible-core/2.15/user_guide/playbooks_reuse_includes.html for details. This
feature will be removed in version 2.16. Deprecation warnings can be disabled by setting
deprecation_warnings=False in ansible.cfg.

PLAY [VK Cloud config] *********************************************************************************

TASK [Gathering Facts] *********************************************************************************
ok: [ubuntu@212.233.95.21]

TASK [docker : include_tasks] **************************************************************************
included: /mnt/d/git/core-course-labs/ansible/roles/docker/tasks/deps.yaml for ubuntu@212.233.95.21

TASK [docker : Ensure dependencies are installed.] *****************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
changed: [ubuntu@212.233.95.21]

TASK [docker : include_tasks] **************************************************************************
included: /mnt/d/git/core-course-labs/ansible/roles/docker/tasks/repo.yaml for ubuntu@212.233.95.21

TASK [docker : Install keys] ***************************************************************************
changed: [ubuntu@212.233.95.21]

TASK [docker : Add docker repo] ************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [ubuntu@212.233.95.21]

TASK [docker : include_tasks] **************************************************************************
included: /mnt/d/git/core-course-labs/ansible/roles/docker/tasks/install.yaml for ubuntu@212.233.95.21

TASK [docker : Check if old deps are absent] ***********************************************************
ok: [ubuntu@212.233.95.21]

TASK [docker : Install docker] *************************************************************************
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  docker-ce-rootless-extras libltdl7 pigz docker-compose-plugin
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
0 upgraded, 4 newly installed, 0 to remove and 216 not upgraded.
changed: [ubuntu@212.233.95.21]

TASK [docker : Install pip packets] ********************************************************************
changed: [ubuntu@212.233.95.21]

TASK [app : Ensure dependencies are installed.] ********************************************************
The following additional packages will be installed:
  wmdocker
The following NEW packages will be installed:
  docker wmdocker
0 upgraded, 2 newly installed, 0 to remove and 216 not upgraded.
changed: [ubuntu@212.233.95.21]

TASK [app : Run python app] ****************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [ubuntu@212.233.95.21]

PLAY RECAP *********************************************************************************************
ubuntu@212.233.95.21       : ok=12   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory

```
dyllas@DyllasDekWork:/mnt/d/git/core-course-labs/ansible$ ansible-inventory -i ./inventory/inv.yaml --list
[WARNING]: Ansible is being run in a world writable directory (/mnt/d/git/core-course-labs/ansible),
ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
{
    "_meta": {
        "hostvars": {
            "ubuntu@212.233.95.21": {
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vk_cloud"
        ]
    },
    "vk_cloud": {
        "children": [
            "type_vkcs_compute_floatingip_associate"
        ],
        "hosts": [
            "ubuntu@212.233.95.21"
        ]
    }
}

```
