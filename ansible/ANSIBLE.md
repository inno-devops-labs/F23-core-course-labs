## `➜ ansible-playbook playbooks/dev/main.yml --diff` output

```bash
PLAY [Prepare docker] *************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************
ok: [vk-cloud]

TASK [docker : Ensure old versions of Docker are not installed.] ******************************************************
ok: [vk-cloud]

TASK [docker : Ensure dependencies are installed.] ********************************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
changed: [vk-cloud]

TASK [docker : include_tasks] *****************************************************************************************
included: /Users/kitt/Study/DevOps/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vk-cloud

TASK [docker : Add Docker apt key.] ***********************************************************************************
changed: [vk-cloud]

TASK [docker : Add Docker repository.] ********************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [vk-cloud]

TASK [docker : Install Docker packages.] ******************************************************************************
skipping: [vk-cloud]

TASK [docker : include_tasks] *****************************************************************************************
included: /Users/kitt/Study/DevOps/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vk-cloud

TASK [docker : Install docker-compose using pip.] *********************************************************************
changed: [vk-cloud]

PLAY RECAP ************************************************************************************************************
vk-cloud                   : ok=8    changed=4    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## `➜ ansible-inventory -i inventory/default.yml --list` output

```bash
{
    "_meta": {
        "hostvars": {
            "vk-cloud": {
                "ansible_host": "2##.###.##.##7",
                "ansible_ssh_private_key_file": "~/.ssh/key.pem",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "vk-cloud"
        ]
    }
}
```
