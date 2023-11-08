# Web App Role

This Ansible role deploys a Docker-based web application.

## Requirements

This role depends on the docker role that should be present and executed before deploying this web_app role. The docker role is responsible for installing and configuring Docker on the target system.

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| app_directory | /opt/web_app | Directory path for the web_app on the target system |
| timezone | UTC | Set the timezone for the web_app |
| web_app_full_wipe | false | If true, the Docker container and image for the web_app will be removed |
| image | bobievnodir/app_python:latest | Docker image of the web_app to be deployed |
| container_name | web_app | Name of the Docker container for the web_app |
| ports | "5000:5000" | Port mapping for the web_app container |

## Usage

1. Add the web_app role to your project's roles directory, or use Ansible Galaxy to install the role.

2. In your playbook, include the role:

```
- hosts: all
  roles:
    - role: docker
    - role: web_app
```

3. (Optional) Define any of the role variables in the playbook or in the host_vars or group_vars directories.

4. Run your playbook:

```
ansible-playbook your-playbook.yml
```

By default, this role deploys the web_app Docker container and ensures it is running. If you set web_app_full_wipe to true, the role will stop and remove the Docker container and its image before redeploying it.