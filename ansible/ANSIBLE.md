## ansible-playbook playbooks/dev/main.yml --diff

```
PLAY [Prepare docker] ***************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************
ok: [localhost]

TASK [docker : Execute apt update] **************************************************************************************************************************
changed: [localhost]

TASK [geerlingguy.pip : Ensure Pip is installed.] ***********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] *****************************************************************************************
changed: [localhost] => (item={'name': 'docker'})
changed: [localhost] => (item={'name': 'docker-compose'})

TASK [geerlingguy.docker : Load OS-specific vars.] **********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************
included: /home/shohjahon/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for localhost

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ********************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **********************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *****************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Add Docker apt key.] *************************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *****************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Add Docker repository.] **********************************************************************************************************
changed: [localhost]

TASK [geerlingguy.docker : Install Docker packages.] ********************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ********************************************************************************
The following additional packages will be installed:
  dbus-user-session docker-buildx-plugin docker-compose-plugin libltdl7
  libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io dbus-user-session docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 11 newly installed, 0 to remove and 165 not upgraded.
changed: [localhost]

TASK [geerlingguy.docker : Install docker-compose plugin.] **************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *******************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Configure Docker daemon options.] ************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***********************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *******************************************************************
skipping: [localhost]

PLAY RECAP **************************************************************************************************************************************************localhost                  : ok=14   changed=5    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0

```


## ansible-inventory -i inventory/default.yml --list

```
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
            "localhost"
        ]
    }
}
```
