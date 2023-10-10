## web_app role
The Role is used to install nessesary depandancies into the host. Ansible Role installs and runs ```wildqueue/devops-hw``` and ```wildqueue/devops-hw-golang``` images.

### Requiremennts:
- Docker
- Python3
- Ansible
- Docker-compose

## Usage Example

```
- hosts: vk_cloud
  become: true
  roles:
    - role: 'web_app'
      image: "wildqueue/devops-hw:tagname"
      ports: "8008:8008"
```