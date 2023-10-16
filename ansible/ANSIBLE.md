## Install requirements
```bash
ansible-galaxy install --force -r requirements.yml
```

## Run geerlingguy_docker playbook
```bash
ansible-playbook playbooks/dev/geerlingguy_docker.yaml
```

<details>
    <summary> Output </summary>

```bash
[arodef@fedora ansible]$ ansible-playbook playbooks/dev/docker_role.yaml 

PLAY [Deploy geerlingguy docker] ********************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
ok: [vm-1]

TASK [geerlingguy.docker : Load OS-specific vars.] **************************************************************************************
ok: [vm-1]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
included: /home/arodef/Projects/core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for vm-1

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ************************************************************
ok: [vm-1]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **************************************************************************
ok: [vm-1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *********************
skipping: [vm-1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ******************************************
ok: [vm-1]

TASK [geerlingguy.docker : Add Docker apt key.] *****************************************************************************************
changed: [vm-1]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ******************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *********************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Add Docker repository.] **************************************************************************************
changed: [vm-1]

TASK [geerlingguy.docker : Install Docker packages.] ************************************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ************************************************************
changed: [vm-1]

TASK [geerlingguy.docker : Install docker-compose plugin.] ******************************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ******************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***********************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Configure Docker daemon options.] ****************************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***************************************************************
ok: [vm-1]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***********************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ***********************************************************************************
changed: [vm-1]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
included: /home/arodef/Projects/core-course-labs/ansible/roles/geerlingguy.docker/tasks/docker-compose.yml for vm-1

TASK [geerlingguy.docker : Check current docker-compose version.] ***********************************************************************
ok: [vm-1]

TASK [geerlingguy.docker : set_fact] ****************************************************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Delete existing docker-compose version if it's different.] ***************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Install Docker Compose (if configured).] *********************************************************************
changed: [vm-1]

TASK [geerlingguy.docker : Get docker group info using getent.] *************************************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ****************************************************
skipping: [vm-1]

TASK [geerlingguy.docker : include_tasks] ***********************************************************************************************
skipping: [vm-1]

PLAY RECAP ******************************************************************************************************************************
vm-1                       : ok=14   changed=5    unreachable=0    failed=0    skipped=14   rescued=0    ignored=0
```
</details>


## Run default_yacloud_compute playbook
```bash
ansible-playbook -i inventory/default_yacloud_compute.yml playbooks/dev/main.yaml --diff
```

<details>
    <summary>  Output </summary>

```bash
PLAY [Prepare docker own role] ******************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************
ok: [terraform-vm-1]

TASK [docker : Install pip] *********************************************************************************************************************
included: /home/arodef/Projects/core-course-labs/ansible/roles/docker/tasks/install_pip.yaml for terraform-vm-1

TASK [docker : Update apt] **********************************************************************************************************************
changed: [terraform-vm-1]

TASK [docker : Install python] ******************************************************************************************************************
ok: [terraform-vm-1]

TASK [docker : Install pip] *********************************************************************************************************************
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
changed: [terraform-vm-1]

TASK [docker : Install docker] ******************************************************************************************************************
included: /home/arodef/Projects/core-course-labs/ansible/roles/docker/tasks/install_docker.yaml for terraform-vm-1

TASK [docker : Install docker] ******************************************************************************************************************
The following additional packages will be installed:
bridge-utils containerd dns-root-data dnsmasq-base git git-man
libcurl3-gnutls liberror-perl libidn11 pigz runc ubuntu-fan
Suggested packages:
ifupdown aufs-tools btrfs-progs cgroupfs-mount | cgroup-lite debootstrap
docker-doc rinse zfs-fuse | zfsutils git-daemon-run | git-daemon-sysvinit
git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
bridge-utils containerd dns-root-data dnsmasq-base docker.io git git-man
libcurl3-gnutls liberror-perl libidn11 pigz runc ubuntu-fan
0 upgraded, 13 newly installed, 0 to remove and 4 not upgraded.
changed: [terraform-vm-1]

TASK [docker : Install docker-compose] **********************************************************************************************************
included: /home/arodef/Projects/core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yaml for terraform-vm-1

TASK [docker : Install docker-compose via pip] **************************************************************************************************
changed: [terraform-vm-1]

PLAY RECAP **************************************************************************************************************************************
terraform-vm-1             : ok=9    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```
</details>


## Inventory Details

```bash
ansible-inventory -i inventory/default_yacloud_compute.yml --list
```

<details>
<summary>Output</summary>

```bash
    {
    "_meta": {
        "hostvars": {
            "terraform-vm-1": {
                "ansible_host": "158.160.46.237"
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
            "terraform-vm-1"
        ]
    }
}
```
</details>


## Dynamic inventory

I set up dynamc inventory for yandex cloud