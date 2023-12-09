# Description

This is a docker role to install docker via apt and configure it with compose via pip



## Tasks

1. Pip
   - install pip
   - install python3
2. docker
   - install required packages via apt
   - maintain a present state
3. docker-compose
   - use built in ansible pip
   - install docker-compose
4. check-version
   - Check all the version of the installed packages
5. Include files
   - Include all the tasks files in the main.yml

## Usage

 - Configure docker for the managed nodes via Ansible

## Requirements

- Ansible
- Ubuntu