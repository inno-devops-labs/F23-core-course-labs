# Docker Role

I implemented a custom Docker role for the project. The role installs Python and Pip to the Ubuntu virtual machine. 
Then using it it sets up Docker and Docker-compose.


## Requirements
Ubuntu 22.04 virtual machine with apt pre-installed (which should be available by default).


## Dependencies

The project assumes that Apt is pre-installed. It also depends on Python3 and Pip.

## Usage

The role can be used just by providing it in the list of roles in yaml config.
```
main.yaml:
- hosts: all
  become: true
  roles:
    - docker
```