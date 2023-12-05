## Ansible

The output of the `ansible-playbook playbooks/dev/main.yml --diff` command

```text
PLAY [Docker] ****************************************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : include_tasks] ************************************************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : include_tasks] ************************************************************************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/install_docker.yml for 127.0.0.1

TASK [docker : Install Docker packages (with downgrade option).] *************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Install docker-compose plugin.] *******************************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Install docker-compose-plugin (with downgrade option).] *******************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Ensure /etc/docker/ directory exists.] ************************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Configure Docker daemon options.] *****************************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Ensure Docker is started and enabled at boot.] ****************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] ************************************************************************************************************

TASK [docker : include_tasks] ************************************************************************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/install_compose.yml for 127.0.0.1

TASK [docker : Check current docker-compose version.] ************************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : set_fact] *****************************************************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Delete existing docker-compose version if it's different.] ****************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Install Docker Compose (if configured).] **********************************************************************************************************************************
changed: [127.0.0.1]

TASK [docker : Get docker group info using getent.] **************************************************************************************************************************************
skipping: [127.0.0.1]

TASK [docker : Check if there are any users to add to the docker group.] *****************************************************************************************************************

TASK [docker : include_tasks] ************************************************************************************************************************************************************
skipping: [127.0.0.1]

PLAY RECAP *******************************************************************************************************************************************************************************
127.0.0.1                  : ok=7    changed=1    unreachable=0    failed=0    skipped=10   rescued=0    ignored=0
```

The output of the `ansible-inventory -i inventory/yacloud_compute.yml --list`

```text
{
    "_meta": {
        "hostvars": {
            "terraform": {
                "ansible_host": "51.250.86.186"
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
            "terraform"
        ]
    }
}
```

### Ansible deploy python-app

```shell
PLAY [Deploy python_app] ***************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************
ok: [terraform]

TASK [docker : include_tasks] *****************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/setup_debian.yml for terraform

TASK [docker : Ensure old versions of Docker are not installed.] *************************************************************************************************
ok: [terraform]

TASK [docker : Ensure dependencies are installed.] ***************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker apt key.] ******************************************************************************************************************************
ok: [terraform]

TASK [docker : Add Docker repository.] ***************************************************************************************************************************
ok: [terraform]

TASK [docker : include_tasks] *****************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/install_docker.yml for terraform

TASK [docker : Install docker-compose] ******************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/docker-compose.yml for web_server

TASK [docker : include_tasks] *****************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/install_compose.yml

TASK [web_app : Wipe] ***********************************************************************************************************
included: /Users/max/labs/ansible/roles/web_app/tasks/0-wipe.yml for web_server

TASK [web_app : Install pip] *************************************************************************************************************************************
The following additional packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-7
  dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7 gcc-7-base
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan4 libatomic1 libbinutils libc-dev-bin libc6 libc6-dev libcc1-0
  libcilkrts5 libdpkg-perl libexpat1 libexpat1-dev libfakeroot
  libfile-fcntllock-perl libgcc-7-dev libgomp1 libisl19 libitm1 liblsan0
  libmpc3 libmpfr6 libmpx2 libpython3-dev libpython3.6 libpython3.6-dev
  libpython3.6-minimal libpython3.6-stdlib libquadmath0 libstdc++-7-dev
  libtsan0 libubsan0 linux-libc-dev make manpages-dev python-pip-whl
  python3-crypto python3-dev python3-distutils python3-keyring
  python3-keyrings.alt python3-lib2to3 python3-secretstorage
  python3-setuptools python3-wheel python3-xdg python3.6 python3.6-dev
  python3.6-minimal
Suggested packages:
  binutils-doc cpp-doc gcc-7-locales debian-keyring g++-multilib
  g++-7-multilib gcc-7-doc libstdc++6-7-dbg gcc-multilib autoconf automake
  libtool flex bison gdb gcc-doc gcc-7-multilib libgcc1-dbg libgomp1-dbg
  libitm1-dbg libatomic1-dbg libasan4-dbg liblsan0-dbg libtsan0-dbg
  libubsan0-dbg libcilkrts5-dbg libmpx2-dbg libquadmath0-dbg glibc-doc bzr
  libstdc++-7-doc make-doc python-crypto-doc gnome-keyring libkf5wallet-bin
  gir1.2-gnomekeyring-1.0 python-secretstorage-doc python-setuptools-doc
  python3.6-venv python3.6-doc binfmt-support
The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-7
  dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7 gcc-7-base
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan4 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0 libcilkrts5
  libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl libgcc-7-dev
  libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpfr6 libmpx2 libpython3-dev
  libpython3.6-dev libquadmath0 libstdc++-7-dev libtsan0 libubsan0
  linux-libc-dev make manpages-dev python-pip-whl python3-crypto python3-dev
  python3-distutils python3-keyring python3-keyrings.alt python3-lib2to3
  python3-pip python3-secretstorage python3-setuptools python3-wheel
  python3-xdg python3.6-dev
The following packages will be upgraded:
  libc6 libexpat1 libpython3.6 libpython3.6-minimal libpython3.6-stdlib
  python3.6 python3.6-minimal
7 upgraded, 58 newly installed, 0 to remove and 97 not upgraded.
changed: [terraform]

TASK [web_app : Install python docker-compose module] ************************************************************************************************************
changed: [terraform]

TASK [web_app : Start with docker-compose] ***********************************************************************************************************************
changed: [terraform]

PLAY RECAP *******************************************************************************************************************************************************
terraform                  : ok=17   changed=5    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0  failed=0    skipped=0    rescued=0    ignored=0   
```

### Ansible deploy go-app

```shell

PLAY [go_app] *******************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *****************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/pip.yml for web_server

TASK [docker : Update apt] ******************************************************************************************************
ok: [web_server]

TASK [docker : Install python] **************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] *****************************************************************************************************
ok: [web_server]

TASK [docker : Install docker] **************************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/docker.yml for web_server

TASK [docker : Install docker via pip] ******************************************************************************************
ok: [web_server]

TASK [docker : Install docker-compose] ******************************************************************************************
included: /Users/max/labs/ansible/roles/docker/tasks/docker-compose.yml for web_server

TASK [docker : Install docker-compose via pip] **********************************************************************************
ok: [web_server]

TASK [web_app : Wipe] ***********************************************************************************************************
included: /Users/max/labs/ansible/roles/web_app/tasks/0-wipe.yml for web_server

TASK [web_app : Check if docker-compose.yml file exists] ************************************************************************
ok: [web_server]

TASK [web_app : Check if Web App directory exists] ******************************************************************************
ok: [web_server]

TASK [web_app : Create directory /app_go] ***************************************************************************************
changed: [web_server]

TASK [web_app : Generate docker-compose from template] **************************************************************************
changed: [web_server]

TASK [web_app : Deliver docker-compose] *****************************************************************************************
changed: [web_server]

RUNNING HANDLER [web_app : Docker Compose restart] ******************************************************************************
changed: [web_server]

PLAY RECAP **********************************************************************************************************************
web_server                 : ok=19   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```