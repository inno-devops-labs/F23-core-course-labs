# My docker role

## General

The role consists of 2 main parts `install_compose` which installs docker-compose and `install_docker` which installs docker. All required packages and vesions are in `defaults/main.yaml`.

## Requirements

- Tested on Ubuntu 18.04 LTS 64-bit
- Ansible 2.15.3
- All other requirements will be installed as part of the role.

## Steps

### Step 1 - Install Docker
1. The role will first install the dependencies specified in `defaults` with `update_cache` flag set to `true` to fetch the latest updates.
2. Adds docker apt key to `apt`.
3. Adds docker repository to `apt`.
4. Installs docker and all related packages.

### Step 2 - Install Docker compse
1. The role will first install the dependencies specified in `defaults` with `update_cache` flag set to `true` to fetch the latest updates.
2. Upgrades `pip` to the latest version.
3. Installs docker-compose via `pip`.

## Usage

Simply use the role in your playbook. Don't forget to grant it root priviledges. Example:

    - name: Deploy custom docker
    become: yes
    hosts: all
    roles:
        - docker
