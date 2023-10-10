# Ansible docker role

## Deployment output

```bash
> ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/self-docker.yml --diff -b

PLAY [run Self-docker] *************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Install pip] ********************************************************************************************************************************
The following packages were automatically installed and are no longer required:
  libltdl7 libslirp0 pigz slirp4netns
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  python3-pip
0 upgraded, 1 newly installed, 0 to remove and 44 not upgraded.
changed: [192.168.64.2]

TASK [docker : Install prerequisites] **********************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Add Docker GPG apt Key] *********************************************************************************************************************
ok: [192.168.64.2]

TASK [docker : Add Docker Repository] **********************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu focal stable

changed: [192.168.64.2]

TASK [docker : Install docker] *****************************************************************************************************************************
The following additional packages will be installed:
  docker-ce-rootless-extras docker-compose-plugin
Suggested packages:
  cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin
0 upgraded, 6 newly installed, 0 to remove and 44 not upgraded.
changed: [192.168.64.2]

TASK [docker : Install docker compose plugin] **************************************************************************************************************
changed: [192.168.64.2]

PLAY RECAP *************************************************************************************************************************************************
192.168.64.2               : ok=7    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Inventory information

```bash
> ansible-inventory -i inventory/default_aws_ec2.yml --list

{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "192.168.64.2"
        ]
    }
}
```

## Dynamic inventory

