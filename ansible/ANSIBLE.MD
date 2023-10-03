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

4.  The inventory (default\_local.yml) includes 1 VM.\
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
