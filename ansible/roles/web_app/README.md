## Deps

- Docker role
- Ansible
- A Unix-like operating system on the target system, tested on Ubuntu.

## Install dependencies

```
ansible-galaxy install -r requirements.yml
```


## Usage


```
- name: Example
  hosts: all
  roles:
    - role: web_app
      service_name: timeapp_python
      image_name: myapp
      host_port: 8080
      internal_port: 8080
```

