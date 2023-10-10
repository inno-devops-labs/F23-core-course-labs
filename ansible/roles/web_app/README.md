# Description

This is a web*app role to install docker via apt and configure it with compose via pip then pull el3os/moscow_time*{python/rust} to be run on the server

## Tasks

1. Stop
   - Check if the docker compose exists
   - Stop the containers
2. Wipe

   - Wiping all the data for the containers

3. Deploy

   - deploy el3os/moscow_time_python with default
   - variables can be passed to deploy the bonus task

4. Include files
   - Include all the tasks files in the main.yml

## Usage

- Configure docker for the managed nodes via Ansible and pull el3os/moscow*time*{python/rust} to be run

## Requirements

- Ansible
- Ubuntu
- "../docker" role
