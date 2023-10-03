### Output of `ansible-playbook -i inventory/default.yaml playbooks/dev/main.yml --diff`
```
PLAY [lab5] ********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [devops-lab-instance.spigin.ru]

TASK [docker : include_tasks] **************************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for devops-lab-instance.spigin.ru

TASK [docker : Update apt cache.] **********************************************
changed: [devops-lab-instance.spigin.ru]

TASK [docker : Install pip.] ***************************************************
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base gcc-12-base
  javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libasan6 libatomic1 libc-dev-bin libc-devtools libc6
  libc6-dev libcc1-0 libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev
  libfakeroot libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgcc-s1
  libgd3 libgomp1 libisl23 libitm1 libjbig0 libjpeg-turbo8 libjpeg8
  libjs-jquery libjs-sphinxdoc libjs-underscore liblsan0 libmpc3 libnsl-dev
  libpython3-dev libpython3.10 libpython3.10-dev libpython3.10-minimal
  libpython3.10-stdlib libquadmath0 libstdc++-11-dev libstdc++6 libtiff5
  libtirpc-dev libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev
  lto-disabled-list make manpages-dev python3-dev python3-wheel python3.10
  python3.10-dev python3.10-minimal rpcsvc-proto zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc python3.10-venv python3.10-doc binfmt-support
Recommended packages:
  libnss-nis libnss-nisplus
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
The following packages will be upgraded:
  gcc-12-base libc6 libgcc-s1 libpython3.10 libpython3.10-minimal
  libpython3.10-stdlib libstdc++6 python3.10 python3.10-minimal
9 upgraded, 64 newly installed, 0 to remove and 73 not upgraded.
changed: [devops-lab-instance.spigin.ru]

TASK [docker : include_tasks] **************************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for devops-lab-instance.spigin.ru

TASK [geerlingguy.docker : Load OS-specific vars.] *****************************
ok: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : include_tasks] **************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for devops-lab-instance.spigin.ru

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***
ok: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 73 not upgraded.
changed: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***
ok: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Add Docker apt key.] ********************************
changed: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Add Docker repository.] *****************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  docker-buildx-plugin docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 73 not upgraded.
changed: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

RUNNING HANDLER [geerlingguy.docker : restart docker] **************************
changed: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [devops-lab-instance.spigin.ru]

TASK [docker : include_tasks] **************************************************
included: /home/vladislav5ik/code-iu/core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for devops-lab-instance.spigin.ru

TASK [geerlingguy.pip : Ensure Pip is installed.] ******************************
ok: [devops-lab-instance.spigin.ru]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] ************
changed: [devops-lab-instance.spigin.ru] => (item={'name': 'docker-compose'})

PLAY RECAP *********************************************************************
devops-lab-instance.spigin.ru : ok=18   changed=8    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```

### Output of `ansible-inventory -i inventory/default.yaml --list`
```
{
    "_meta": {
        "hostvars": {
            "devops-lab-instance.spigin.ru": {
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex_vms"
        ]
    },
    "yandex_vms": {
        "hosts": [
            "devops-lab-instance.spigin.ru"
        ]
    }
}
```
