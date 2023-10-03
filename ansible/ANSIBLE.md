# Ansible outputs

## Last 50 lines of the output:

```
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [ubuntu@84.23.53.144]

TASK [docker : include_tasks] ******************************************************************************************
included: /mnt/d/Study/F23/Devops/core-course-labs/ansible/roles/docker/tasks/install.yaml for ubuntu@84.23.53.144

TASK [docker : Ensure unnecessary, unofficial or old packages are removed] *********************************************
ok: [ubuntu@84.23.53.144]

TASK [docker : Install docker] *****************************************************************************************
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  docker-ce-rootless-extras libltdl7 pigz docker-compose-plugin
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
0 upgraded, 4 newly installed, 0 to remove and 216 not upgraded.
changed: [ubuntu@84.23.53.144]

TASK [docker : Install pip packets] ************************************************************************************
changed: [ubuntu@84.23.53.144]

TASK [apps : Ensure dependencies are installed.] ***********************************************************************
The following additional packages will be installed:
  wmdocker
The following NEW packages will be installed:
  docker wmdocker
0 upgraded, 2 newly installed, 0 to remove and 216 not upgraded.
changed: [ubuntu@84.23.53.144]

TASK [apps : Run application] ******************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

[DEPRECATION WARNING]: The container_default_behavior option will change its default value from "compatibility" to
"no_defaults" in community.general 3.0.0. To remove this warning, please specify an explicit value for it now. This
feature will be removed from community.general in version 3.0.0. Deprecation warnings can be disabled by setting
deprecation_warnings=False in ansible.cfg.
changed: [ubuntu@84.23.53.144]

PLAY RECAP *************************************************************************************************************
ubuntu@84.23.53.144        : ok=12   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory

`ansible-playbook main.yaml -i ./inventory/inventory.yaml --diff`

``` 
ml --list
[WARNING]: Ansible is being run in a world writable directory (/mnt/d/Study/F23/Devops/core-course-labs/ansible),
ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
{
    "_meta": {
        "hostvars": {
            "ubuntu@84.23.53.144": {
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
            "ubuntu@84.23.53.144"
        ]
    }
}
```
