# Docker role description
> The tasks I defined are responsible for adding the Docker GPG apt key, adding the Docker repository to the list of available package sources, and then updating the package cache and installing the docker-ce package on a target Ubuntu Linux system. Also, installing pip and docker-compose.

## Tasks

1. install_pip.yml
    - install pip 

2. install_docker.yml
    - add GPG apt key ( for protection )
    - add Docker repository
    - Update cache and install docker-ce

3. install_compose.yml
    - installing docker compose using pip

## Usage 

In order to apply the configurations to the server, you should run the following cmd : 

```sh
ansible-playbook /Users/m4k4rich/core-course-labs/ansible/playbooks/dev/main.yaml
```
