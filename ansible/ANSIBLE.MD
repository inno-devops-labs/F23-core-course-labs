# Task 1

1.  Created file structure.
2.  Installed Ansible and followed the getting started guide.

```bash
pipx install ansible-core
```

3.  Using the example role: geerlingguy.docker.

```bash
ansible-galaxy install geerlingguy.docker
```

4.  The inventory (default\_local.yml) includes 2 VMs.\
    The VM was setup with the DOE labs ssh key using ssh-copy-id.\
    The playbook:

```yaml
- name: Deploy Docker
  hosts: vms
  become: true
  become_method: sudo
  roles:
  - geerlingguy.docker
```

Running it like (using sudo to gain root privileges for package installation):

```bash
ansible-playbook playbooks/dev/main.yml  --ask-become-pass
```

Result:
`vm01 : ok=12   changed=5    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0`

# Task 2

1.  Custom Docker role includes 3 tasks:
    install docker, install docker-compose and main (which incudes installing pip).
    The deployment is successfull.

2.  Created this and `ansible/roles/docker/README.md` files

3.  I added a second VM at this step.

```yaml
 ______________________ 
< PLAY [Deploy Docker] >
 ---------------------- 

 ________________________ 
< TASK [Gathering Facts] >
 ------------------------ 

ok: [vm01]
ok: [vm02]
 _____________________________ 
< TASK [docker : Install pip] >
 ----------------------------- 

ok: [vm02]
ok: [vm01]
 _______________________________ 
< TASK [docker : include_tasks] >
 ------------------------------- 

included: /home/tea/Documents/inno5/DOE/DOE-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm01, vm02
 _________________________________________________ 
< TASK [docker : Install Docker and dependencies] >
 ------------------------------------------------- 

ok: [vm02]
ok: [vm01]
 ____________________________________ 
< TASK [docker : Add Docker GPG key] >
 ------------------------------------ 

ok: [vm01]
ok: [vm02]
 _______________________________________ 
< TASK [docker : Add Docker repository] >
 --------------------------------------- 

ok: [vm01]
ok: [vm02]
 ________________________________ 
< TASK [docker : Install Docker] >
 -------------------------------- 

ok: [vm01]
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 95 not upgraded.
changed: [vm02]
 __________________________________________________ 
< TASK [docker : Install Docker Module for Python] >
 -------------------------------------------------- 

ok: [vm01]
changed: [vm02]
 _______________________________ 
< TASK [docker : include_tasks] >
 ------------------------------- 

included: /home/tea/Documents/inno5/DOE/DOE-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm01, vm02
 ________________________________________ 
< TASK [docker : Install Docker Compose] >
 ---------------------------------------- 

ok: [vm01]
changed: [vm02]
 ____________ 
< PLAY RECAP >
 ------------ 

vm01                       : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
vm02                       : ok=10   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

4.  :

```json
{
    "_meta": {
        "hostvars": {
            "vm01": {
                "ansible_host": "10.244.1.39",
                "ansible_user": "doe"
            },
            "vm02": {
                "ansible_host": "10.244.1.41",
                "ansible_user": "doe"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vms"
        ]
    },
    "vms": {
        "hosts": [
            "vm01",
            "vm02"
        ]
    }
}
```
