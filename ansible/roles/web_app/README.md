# Web app role
This role will deploy or wipe docker-compose container on host.

## Requirements
- docker role
- ansible on local machine

## How to use
Add this role to your playbook and run 


```bash
ansible-playbook -i inventory main.yml
```

## Variables
- `docker_image` - image to deploy
- `directory_name` - name of directory on target host, where container will be located
- `docker_ports` - ports which should be forwarded from docker to remote machine
- `wipe_docker_compose` - whether to wipe previous instance of container

