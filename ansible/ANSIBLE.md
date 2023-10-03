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
