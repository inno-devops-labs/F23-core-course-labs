# Ansible Playbook and Role Documentation

This document provides an overview of the Ansible playbook and roles used in your infrastructure automation.

## Playbook: `main.yaml`

- **Hosts**: `devops`
- **Privilege Escalation**: Enabled (become: true)

### Roles

#### Role: `docker`

This role is responsible for installing Docker on target hosts.

- **Tasks**:

    - Install aptitude
    - Install required system packages
    - Add Docker GPG apt Key
    - Add Docker Repository
    - Update apt and install docker-ce
    - Install Docker Module for Python

#### Role: `web_app`

This role is responsible for managing the application container.

- **Tasks**:

    - Pull application Docker image (`trihlebdv/dev_hw3`)
    - Create the application container with the name `myapp` and expose port 5000

## How to Run the Playbook

1. Ensure that Ansible is installed on your control machine.

2. Make sure you have an inventory file (`hosts`) that defines the `devops` group with the appropriate target hosts.

3. Execute the playbook using the following command:

   ```bash
   ansible-playbook playbook/main.yaml


## ansible-playbook playbooks/dev/main.yaml --diff

```bash
changed: [62.84.126.253]
 __________________________________________________
< TASK [docker : Install Docker Module for Python] >
 --------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [62.84.126.253]
 ________________________________________________
< TASK [web_app : Pull application Docker image] >
 ------------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

changed: [62.84.126.253]
 _______________________________________________
< TASK [web_app : Create application container] >
 -----------------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [62.84.126.253]
 ____________
< PLAY RECAP >
 ------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

62.84.126.253              : ok=9    changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
## ansible-inventory -i /etc/myhosts.txt --list

```bash
{
    "_meta": {
        "hostvars": {
            "62.84.126.253": {
                "ansible_ssh_user": "devops"
            }
        }
    },
    "all": {
        "children": [
            "devops",
            "ungrouped"
        ]
    },
    "devops": {
        "hosts": [
            "62.84.126.253"
        ]
    }
}
```