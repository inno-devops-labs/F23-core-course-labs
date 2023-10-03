

### Requirements:
- Ansible version compatible with the roles used
- Root/sudo privileges to execute apt update
- Docker package dependencies
- Internet access to download packages

### Pre-install

```
ansible-galaxy install geerlingguy.pip
ansible-galaxy install geerlingguy.docker
```

### Usage:

1. Execute apt update: This task updates the package cache on the target machine using the Ansible apt module. It requires root or sudo privileges to be executed.

2. Install Docker using apt: This task imports the "geerlingguy.docker" Ansible role, which installs Docker on the target machine using the apt package manager. It sets the "docker_install_compose" and "docker_install_compose_plugin" variables to false, indicating that Docker Compose and Docker Compose plugin installations are not required in this case.

3. Install Docker Compose using pip: This task imports the "geerlingguy.pip" Ansible role, which installs Docker Compose on the target machine using the pip package manager. It uses the "docker" and "docker-compose" packages to be installed via pip.
