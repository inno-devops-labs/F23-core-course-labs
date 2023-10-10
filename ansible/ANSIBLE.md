# ANSIBLE
## Task 1

### Installing ansible
Installing pipx:
```
brew install pipx
pipx ensurepath
```

Installing ansible:
```
pipx install ansible-core
```
Checking ansible version:
```
ansible --version
```
Output:
```
arseniyrubtsov@MacBook-Pro-Arseniy ansible % ansible --version
ansible [core 2.15.4]
  config file = /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/ansible.cfg
  configured module search path = ['/Users/arseniyrubtsov/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /Users/arseniyrubtsov/.local/pipx/venvs/ansible-core/lib/python3.11/site-packages/ansible
  ansible collection location = /Users/arseniyrubtsov/.ansible/collections:/usr/share/ansible/collections
  executable location = /Users/arseniyrubtsov/.local/bin/ansible
  python version = 3.11.5 (main, Aug 24 2023, 15:09:45) [Clang 14.0.3 (clang-1403.0.22.14.1)] (/Users/arseniyrubtsov/.local/pipx/venvs/ansible-core/bin/python)
  jinja version = 3.1.2
  libyaml = True
```
Then I created the proposed folders structure in the lab and copied existing docker role from given repository. (existing Ansible role for Docker from ansible-galaxy as a template)

Then I utilized the terraform from the previous lab terraform/cloud-terraform:
```
terraform apply
```
which gave me the output:
```
Outputs:
instance_fip = "84.23.55.42"
```

Made some changes in configs:
default_hosts.yml
```
vk-cloud:
  hosts:
    84.23.55.42
  vars:
    ansible_user: ubuntu
    ansible_ssh_private_key_file: ~/.ssh/id_rsa
```
playbooks/dev/main.yaml
```
- hosts: vk-cloud
  roles:
    - role: 'roles/docker'
  become: true
```
ansible.cfg
```
[defaults]
action_warnings = True
inventory = inventory/default_hosts.yml
roles_path = roles
```
Also I needed to create my ssh key because VK Cloud gives .pem and I lost it:
```
ssh-keygen -t rsa -b 2048 -C "a.rubtsov@innopolis.university"
```
Uploaded the public key to VK Cloud and then connected to check that the VM is working:
```
chmod 400 ~/.ssh/id_rsa
ssh -i id_rsa ubuntu@84.23.55.42
```

Output:
```
arseniyrubtsov@MacBook-Pro-Arseniy .ssh % ssh -i id_rsa ubuntu@84.23.55.42
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Oct  3 16:49:54 UTC 2023

  System load:  0.3017578125      Processes:                99
  Usage of /:   41.8% of 7.42GB   Users logged in:          0
  Memory usage: 14%               IPv4 address for docker0: 172.17.0.1
  Swap usage:   0%                IPv4 address for ens3:    192.168.199.12


223 updates can be applied immediately.
149 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


Last login: Tue Oct  3 16:49:17 2023 from 185.14.30.39
```
After that I started the ansible playbook using command:
```
ansible-playbook playbooks/dev/main.yaml
```

Output:
```
arseniyrubtsov@MacBook-Pro-Arseniy ansible % ansible-playbook playbooks/dev/main.yaml
[WARNING]: Invalid characters were found in group names but not replaced, use -vvvv to see details

PLAY [vk-cloud] *******************************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************************
ok: [84.23.55.42]

TASK [docker : Load OS-specific vars.] ********************************************************************************************************************************************************************
ok: [84.23.55.42]

TASK [docker : include_tasks] *****************************************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : include_tasks] *****************************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker/tasks/setup-Debian.yml for 84.23.55.42

TASK [docker : Ensure old versions of Docker are not installed.] ******************************************************************************************************************************************
ok: [84.23.55.42]

TASK [docker : Ensure dependencies are installed.] ********************************************************************************************************************************************************
ok: [84.23.55.42]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ************************************************************************************************************************
ok: [84.23.55.42]

TASK [docker : Add Docker apt key.] ***********************************************************************************************************************************************************************
changed: [84.23.55.42]

TASK [docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Add Docker repository.] ********************************************************************************************************************************************************************
changed: [84.23.55.42]

TASK [docker : Install Docker packages.] ******************************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Install Docker packages (with downgrade option).] ******************************************************************************************************************************************
changed: [84.23.55.42]

TASK [docker : Install docker-compose plugin.] ************************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************************************************************
changed: [84.23.55.42]

TASK [docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Configure Docker daemon options.] **********************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************************************************************
ok: [84.23.55.42]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************************************************************

RUNNING HANDLER [docker : restart docker] *****************************************************************************************************************************************************************
changed: [84.23.55.42]

TASK [docker : include_tasks] *****************************************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Get docker group info using getent.] *******************************************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : Check if there are any users to add to the docker group.] **********************************************************************************************************************************
skipping: [84.23.55.42]

TASK [docker : include_tasks] *****************************************************************************************************************************************************************************
skipping: [84.23.55.42]

PLAY RECAP ************************************************************************************************************************************************************************************************
84.23.55.42                : ok=12   changed=5    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```

After that I connected to VM using ssh:
```
ssh -i id_rsa ubuntu@84.23.55.42
```
And checked docker version:
```
docker --version
```
Output:
```
ubuntu@compute-instance:~$ docker --version
Docker version 24.0.6, build ed223bc
```
And docker compose:
```
docker compose
```
Output:
```
ubuntu@compute-instance:~$ docker compose

Usage:  docker compose [OPTIONS] COMMAND

Define and run multi-container applications with Docker.

Options:
      --ansi string                Control when to print ANSI control
                                   characters ("never"|"always"|"auto")
                                   (default "auto")
      --compatibility              Run compose in backward compatibility mode
      --dry-run                    Execute command in dry run mode
      --env-file stringArray       Specify an alternate environment file.
  -f, --file stringArray           Compose configuration files
      --parallel int               Control max parallelism, -1 for
                                   unlimited (default -1)
      --profile stringArray        Specify a profile to enable
      --progress string            Set type of progress output (auto,
                                   tty, plain, quiet) (default "auto")
      --project-directory string   Specify an alternate working directory
                                   (default: the path of the, first
                                   specified, Compose file)
  -p, --project-name string        Project name

Commands:
  build       Build or rebuild services
  config      Parse, resolve and render compose file in canonical format
  cp          Copy files/folders between a service container and the local filesystem
  create      Creates containers for a service.
  down        Stop and remove containers, networks
  events      Receive real time events from containers.
  exec        Execute a command in a running container.
  images      List images used by the created containers
  kill        Force stop service containers.
  logs        View output from containers
  ls          List running compose projects
  pause       Pause services
  port        Print the public port for a port binding.
  ps          List containers
  pull        Pull service images
  push        Push service images
  restart     Restart service containers
  rm          Removes stopped service containers
  run         Run a one-off command on a service.
  start       Start services
  stop        Stop services
  top         Display the running processes
  unpause     Unpause services
  up          Create and start containers
  version     Show the Docker Compose version information
  wait        Block until the first service container stops

Run 'docker compose COMMAND --help' for more information on a command.
```
And exited:
```
ubuntu@compute-instance:~$ exit
logout
```

## Task 2

I decided to use the proposed solution from geerlingguy at first I installed the needed roles:
```
ansible-galaxy install geerlingguy.docker
ansible-galaxy install geerlingguy.pip
```
Then I created a new folder /docker-custom-role in /roles.
After that I recreated terraform and obtained new ip.
```
Outputs:

instance_fip = "89.208.84.38"
```
After that changed configs with ip and role which I want to start. Configured my docker-custom-role with tasks: install_pip, install_docker and install_compose. Included this tasks in main.yml.

And after several attempts successfully run the ansible:
```
ansible-playbook playbooks/dev/main.yaml 
```
Output:
```
arseniyrubtsov@MacBook-Pro-Arseniy ansible % ansible-playbook playbooks/dev/main.yaml

PLAY [vk_cloud] *******************************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************************
The authenticity of host '89.208.84.38 (89.208.84.38)' can't be established.
ED25519 key fingerprint is SHA256:0EFb4c/suA684LjOGRiM3aqvA4sJCPjqpuCRKFk59wc.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [89.208.84.38]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_pip.yml for 89.208.84.38

TASK [docker-custom-role : Installing pip using apt] ******************************************************************************************************************************************************
changed: [89.208.84.38]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_docker.yml for 89.208.84.38

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 89.208.84.38

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************************************************
changed: [89.208.84.38]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************************************************
changed: [89.208.84.38]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************************************************
changed: [89.208.84.38]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] *****************************************************************************************************************************************************
changed: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_compose.yml for 89.208.84.38

TASK [geerlingguy.pip : Ensure Pip is installed.] *********************************************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] ***************************************************************************************************************************************
changed: [89.208.84.38] => (item={'name': 'docker-compose'})

PLAY RECAP ************************************************************************************************************************************************************************************************
89.208.84.38               : ok=17   changed=6    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```

Then I connected using ssh to VM and checked that everything works fine.

```
arseniyrubtsov@MacBook-Pro-Arseniy .ssh % ssh -i id_rsa ubuntu@89.208.84.38
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-46-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Oct  3 19:01:00 UTC 2023

  System load:  0.03369140625     Processes:                99
  Usage of /:   41.3% of 7.42GB   Users logged in:          0
  Memory usage: 14%               IPv4 address for docker0: 172.17.0.1
  Swap usage:   0%                IPv4 address for ens3:    192.168.199.3


225 updates can be applied immediately.
151 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


Last login: Tue Oct  3 18:58:56 2023 from 185.14.30.39
ubuntu@compute-instance:~$ docker --version
Docker version 24.0.6, build ed223bc
ubuntu@compute-instance:~$ pip --version
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
ubuntu@compute-instance:~$ pip freeze
attrs==21.2.0
Automat==20.2.0
Babel==2.8.0
bcrypt==3.2.0
blinker==1.4
certifi==2020.6.20
cffi==1.16.0
chardet==4.0.0
charset-normalizer==3.3.0
click==8.0.3
cloud-init==22.2
colorama==0.4.4
command-not-found==0.3
configobj==5.0.6
constantly==15.1.0
cryptography==3.4.8
dbus-python==1.2.18
distro==1.7.0
distro-info===1.1build1
docker==6.1.3
docker-compose==1.29.2
dockerpty==0.4.1
docopt==0.6.2
httplib2==0.20.2
hyperlink==21.0.0
idna==3.3
importlib-metadata==4.6.4
incremental==21.3.0
jeepney==0.7.1
Jinja2==3.0.3
jsonpatch==1.32
jsonpointer==2.0
jsonschema==3.2.0
keyring==23.5.0
launchpadlib==1.10.16
lazr.restfulclient==0.14.4
lazr.uri==1.0.6
MarkupSafe==2.0.1
more-itertools==8.10.0
netifaces==0.11.0
oauthlib==3.2.0
packaging==23.2
paramiko==3.3.1
pexpect==4.8.0
ptyprocess==0.7.0
pyasn1==0.4.8
pyasn1-modules==0.2.1
pycparser==2.21
PyGObject==3.42.1
PyHamcrest==2.0.2
PyJWT==2.4.0
PyNaCl==1.5.0
pyOpenSSL==21.0.0
pyparsing==2.4.7
pyrsistent==0.18.1
pyserial==3.5
python-apt==2.3.0+ubuntu2.1
python-debian===0.1.43ubuntu1
python-dotenv==0.21.1
pytz==2022.1
PyYAML==5.4.1
requests==2.31.0
SecretStorage==3.3.1
service-identity==18.1.0
six==1.16.0
sos==4.3
ssh-import-id==5.11
systemd-python==234
texttable==1.7.0
Twisted==22.1.0
ubuntu-advantage-tools==27.9
ufw==0.36.1
unattended-upgrades==0.1
urllib3==1.26.5
wadllib==1.3.6
websocket-client==0.59.0
zipp==1.0.0
zope.interface==5.4.0
```


### Deployment Output:
Using command:
```sh
ansible-playbook <path_to your_playbook> --diff
```
Output:
```
arseniyrubtsov@MacBook-Pro-Arseniy ansible % ansible-playbook playbooks/dev/main.yaml --diff

PLAY [vk_cloud] *******************************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************************
The authenticity of host '89.208.84.38 (89.208.84.38)' can't be established.
ED25519 key fingerprint is SHA256:VL8rUFzQ2rwRNhVn95olX65ijpfHxY1xr77w3d9CqL4.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [89.208.84.38]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_pip.yml for 89.208.84.38

TASK [docker-custom-role : Installing pip using apt] ******************************************************************************************************************************************************
The following additional packages will be installed:
  python3-wheel
Recommended packages:
  build-essential python3-dev
The following NEW packages will be installed:
  python3-pip python3-wheel
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
changed: [89.208.84.38]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_docker.yml for 89.208.84.38

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 89.208.84.38

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************************************************
changed: [89.208.84.38]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [89.208.84.38]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************************************************
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  libltdl7 pigz docker-buildx-plugin docker-compose-plugin slirp4netns
The following NEW packages will be installed:
  containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras
0 upgraded, 4 newly installed, 0 to remove and 216 not upgraded.
changed: [89.208.84.38]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] *****************************************************************************************************************************************************
changed: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************************************************
skipping: [89.208.84.38]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [89.208.84.38]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_compose.yml for 89.208.84.38

TASK [geerlingguy.pip : Ensure Pip is installed.] *********************************************************************************************************************************************************
ok: [89.208.84.38]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] ***************************************************************************************************************************************
changed: [89.208.84.38] => (item={'name': 'docker-compose'})

PLAY RECAP ************************************************************************************************************************************************************************************************
89.208.84.38               : ok=17   changed=6    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0  
```

### Inventory Details:

Using command:
```sh
ansible-inventory -i <name_of_your_inventory_file>.yaml --list
```
Output:
```
arseniyrubtsov@MacBook-Pro-Arseniy ansible % ansible-inventory -i inventory/default_hosts.yml --list
{
    "_meta": {
        "hostvars": {
            "89.208.84.38": {
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
        "hosts": [
            "89.208.84.38"
        ]
    }
}
```
## Bonus task

### Dynamic Inventory

It seems like VK Cloud doesn't support the dynamic inventory by itself, probably something is possible using OpenStack. But I really wanted to get the bonus points so I implemented dynamic inventory using .tfstates file. 

There is a github repo: https://github.com/adammck/terraform-inventory with terraform-inventory.

You can install terraform inventory using command:
```
brew install terraform-inventory
```
```
terraform-inventory --list
```
After that there will be an issue with it:
```
Error reading tfstate file: 0.12 format error: <nil>; pre-0.12 format error: <nil> (nil error means no content/modules found in the respective format)
```
Which can be fixed with script provided in this discussion:
https://github.com/adammck/terraform-inventory/issues/121

Script:
```sh
#!/bin/bash

# https://github.com/adammck/terraform-inventory/issues/121#issuecomment-749663776

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TERRAFORM_INVENTORY=`which terraform-inventory`
TF_STATE="$CURRENT_DIR/../../terraform/cloud-terraform"
"$TERRAFORM_INVENTORY" "$@" "$TF_STATE"
```
After adding it to inventory folder it is possible to pass the inventory file to ansible using this command:
```
ansible-playbook --inventory-file=./inventory/dynamic_inventory.sh playbooks/dev/main.yaml
```
Also you need to specify the hosts in playbooks/dev/main.yaml which can be taken from this command output:
```
terraform-inventory --list ../terraform/cloud-terraform
```
Output:
```
"all":
  "hosts":["192.168.199.5","89.208.84.38"],
  "vars":
    "instance_fip":"89.208.84.38",
"compute":["192.168.199.5"],
"compute_0":["192.168.199.5"],
"fip":["89.208.84.38"],
"fip_0":["89.208.84.38"],
"type_vkcs_compute_floatingip_associate":["89.208.84.38"],
"type_vkcs_compute_instance":["192.168.199.5"]
```
In main.yaml we can specify what we want to access:

```
hosts : type_vkcs_compute_floatingip_associates
```
Or use
```
hosts : all 
```
then the local IP-addresses of servers will be ignored.

<br>
<br>
<br>
<br>
<br>

# ANSIBLE 2

## Task 1: Application Deployment
## Install the dependencies for this task:
```
ansible-galaxy collection install community.docker
```

Output from your deployment command:
```
arseniyrubtsov@MacBook-Pro-Arseniy ansible % ansible-playbook --inventory-file=./inventory/dynamic_inventory.sh playbooks/dev/app_python/main.yaml

PLAY [Deploy Python App] **********************************************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************************************
The authenticity of host '95.163.251.170 (95.163.251.170)' can't be established.
ED25519 key fingerprint is SHA256:i+qmENQzafgrJEx5ZABcHCl1SMHEhy5uKT6BKEmwgGo.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [95.163.251.170]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_pip.yml for 95.163.251.170

TASK [docker-custom-role : Installing pip using apt] ******************************************************************************************************************************************************
changed: [95.163.251.170]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_docker.yml for 95.163.251.170

TASK [geerlingguy.docker : Load OS-specific vars.] ********************************************************************************************************************************************************
ok: [95.163.251.170]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for 95.163.251.170

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ******************************************************************************************************************************
ok: [95.163.251.170]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ********************************************************************************************************************************************
ok: [95.163.251.170]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ************************************************************************************************************
ok: [95.163.251.170]

TASK [geerlingguy.docker : Add Docker apt key.] ***********************************************************************************************************************************************************
changed: [95.163.251.170]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Add Docker repository.] ********************************************************************************************************************************************************
changed: [95.163.251.170]

TASK [geerlingguy.docker : Install Docker packages.] ******************************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ******************************************************************************************************************************
changed: [95.163.251.170]

TASK [geerlingguy.docker : Install docker-compose plugin.] ************************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *****************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Configure Docker daemon options.] **********************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *********************************************************************************************************************************
ok: [95.163.251.170]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *****************************************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] *****************************************************************************************************************************************************
changed: [95.163.251.170]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Get docker group info using getent.] *******************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] **********************************************************************************************************************
skipping: [95.163.251.170]

TASK [geerlingguy.docker : include_tasks] *****************************************************************************************************************************************************************
skipping: [95.163.251.170]

TASK [docker-custom-role : include_tasks] *****************************************************************************************************************************************************************
included: /Users/arseniyrubtsov/Desktop/core-course-labs-devops/ansible/roles/docker-custom-role/tasks/install_compose.yml for 95.163.251.170

TASK [geerlingguy.pip : Ensure Pip is installed.] *********************************************************************************************************************************************************
ok: [95.163.251.170]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] ***************************************************************************************************************************************
changed: [95.163.251.170] => (item={'name': 'docker-compose'})

TASK [web_app : Pull Docker image] ************************************************************************************************************************************************************************
changed: [95.163.251.170]

TASK [web_app : Run Docker container] *********************************************************************************************************************************************************************
changed: [95.163.251.170]

PLAY RECAP ************************************************************************************************************************************************************************************************
95.163.251.170             : ok=19   changed=8    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0  
```