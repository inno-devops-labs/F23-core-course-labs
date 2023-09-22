# Lab 5

## 

## ansible-inventory -i inventory/yacloud_compute.yml --list -vvvvv

```yaml
ansible-inventory [core 2.15.4]
  config file = /home/user/core-course-labs/ansible/ansible.cfg
  configured module search path = ['/home/user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/user/.local/lib/python3.11/site-packages/ansible
  ansible collection location = /home/user/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/user/.local/bin/ansible-inventory
  python version = 3.11.5 (main, Aug 28 2023, 00:00:00) [GCC 13.2.1 20230728 (Red Hat 13.2.1-1)] (/usr/bin/python3)
  jinja version = 3.1.2
  libyaml = True
Using /home/user/core-course-labs/ansible/ansible.cfg as config file
setting up inventory plugins
Loading collection ansible.builtin from 
host_list declined parsing /home/user/core-course-labs/ansible/inventory/yacloud_compute.yml as it did not pass its verify_file() method
script declined parsing /home/user/core-course-labs/ansible/inventory/yacloud_compute.yml as it did not pass its verify_file() method
Using inventory plugin 'yacloud_compute' to process inventory source '/home/user/core-course-labs/ansible/inventory/yacloud_compute.yml'
Parsed /home/user/core-course-labs/ansible/inventory/yacloud_compute.yml inventory source with auto plugin
{
    "_meta": {
        "hostvars": {
            "test": {
                "ansible_host": "130.193.50.170",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "test"
        ]
    }
}
```
