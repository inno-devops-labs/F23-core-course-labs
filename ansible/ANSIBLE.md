```
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml

PLAY [Install docker on yandex] ******************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************
fatal: [51.250.29.149]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: tyakhshigulov@51.250.29.149: Permission denied (publickey).", "unreachable": true}

PLAY RECAP ***************************************************************************************************************************
51.250.29.149              : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0   

(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml
[WARNING]:  * Failed to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml with auto plugin:
We were unable to read either as JSON nor YAML, these are the errors we got from each: JSON: Expecting value: line 1 column 2 (char
1)  Syntax Error while loading YAML.   did not find expected <document start>  The error appears to be in
'/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml': line 2, column 1, but may be elsewhere in
the file depending on the exact syntax problem.  The offending line appears to be:  [yandex] 51.250.29.149 ^ here
[WARNING]:  * Failed to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml with yaml plugin:
We were unable to read either as JSON nor YAML, these are the errors we got from each: JSON: Expecting value: line 1 column 2 (char
1)  Syntax Error while loading YAML.   did not find expected <document start>  The error appears to be in
'/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml': line 2, column 1, but may be elsewhere in
the file depending on the exact syntax problem.  The offending line appears to be:  [yandex] 51.250.29.149 ^ here
[WARNING]:  * Failed to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml with ini plugin:
Invalid host pattern '---' supplied, '---' is normally a sign this is a YAML file.
[WARNING]: Unable to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml as an inventory
source
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Install docker on yandex] ******************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************
fatal: [51.250.29.149]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: tyakhshigulov@51.250.29.149: Permission denied (publickey).", "unreachable": true}

PLAY RECAP ***************************************************************************************************************************
51.250.29.149              : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0   

(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml
[WARNING]:  * Failed to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml with auto plugin:
no root 'plugin' key found, '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml' is not a valid
YAML inventory plugin config file
[WARNING]:  * Failed to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml with yaml plugin:
Invalid data from file, expected dictionary and got:  51.250.29.149
[WARNING]:  * Failed to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml with ini plugin:
Invalid host pattern 'yandex:' supplied, ending in ':' is not allowed, this character is reserved to provide a port.
[WARNING]: Unable to parse /Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/inventory/default_yandex.yml as an inventory
source
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Install docker on yandex] ******************************************************************************************************
skipping: no hosts matched

PLAY RECAP ***************************************************************************************************************************

(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml

PLAY [Install docker on yandex] ******************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************
fatal: [main]: FAILED! => {"msg": "the field 'port' has an invalid value (51.250.29.149), and could not be converted to an int.The error was: invalid literal for int() with base 10: '51.250.29.149'. invalid literal for int() with base 10: '51.250.29.149'"}

PLAY RECAP ***************************************************************************************************************************
main                       : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml

PLAY [Install docker on yandex] ******************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************
ok: [main]

TASK [ping] **************************************************************************************************************************
ok: [main]

PLAY RECAP ***************************************************************************************************************************
main                       : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml
ERROR! couldn't resolve module/action 'docker'. This often indicates a misspelling, missing collection, or incorrect module path.

The error appears to be in '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/playbooks/docker/main.yml': line 4, column 7, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  tasks:
    - docker:
      ^ here
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/main.yml
ERROR! A malformed block was encountered while loading a block. The ds (['docker']) should be a dict but was a <class 'list'>
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml 
ERROR! unexpected parameter type in action: <class 'ansible.parsing.yaml.objects.AnsibleSequence'>

The error appears to be in '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/roles/docker/tasks/main.yml': line 1, column 3, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:


- name: Install
  ^ here
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml
ERROR! unexpected parameter type in action: <class 'ansible.parsing.yaml.objects.AnsibleSequence'>

The error appears to be in '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/roles/docker/tasks/main.yml': line 1, column 3, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:


- name: Install
  ^ here
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml
ERROR! unexpected parameter type in action: <class 'ansible.parsing.yaml.objects.AnsibleSequence'>

The error appears to be in '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/roles/docker/tasks/main.yml': line 2, column 3, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:


- name: Install
  ^ here
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml
ERROR! unexpected parameter type in action: <class 'ansible.parsing.yaml.objects.AnsibleSequence'>

The error appears to be in '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/roles/docker/tasks/main.yml': line 2, column 3, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

---
- name: Install
  ^ here
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml
ERROR! unexpected parameter type in action: <class 'ansible.parsing.yaml.objects.AnsibleSequence'>

The error appears to be in '/Users/tyakhshigulov/PycharmProjects/devops-labs/ansible/roles/docker/tasks/main.yml': line 2, column 3, but may
be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

---
- name: Install oisdlfas
  ^ here
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml
ERROR! the field 'hosts' is required but was not set
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml 
ERROR! the field 'hosts' is required but was not set
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook -i inventory/default_yandex.yml playbooks/docker/install-docker.yml

PLAY [Task2] *************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************
ok: [main]

TASK [docker : Install pip] **********************************************************************************************************
changed: [main]

TASK [docker : Install docker] *******************************************************************************************************
changed: [main]

TASK [docker : Install compose] ******************************************************************************************************
changed: [main]

PLAY RECAP ***************************************************************************************************************************
main                       : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(venv) ➜  ansible git:(lab5) ✗ ansible-playbook <path_to your_playbook> --diff
zsh: no such file or directory: path_to
(venv) ➜  ansible git:(lab5) ✗ ansible-playbook playbooks/docker/install-docker.yml --diff

PLAY [Task2] *************************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************
ok: [main]

TASK [docker : Install pip] **********************************************************************************************************
ok: [main]

TASK [docker : Install docker] *******************************************************************************************************
changed: [main]

TASK [docker : Install compose] ******************************************************************************************************
changed: [main]

PLAY RECAP ***************************************************************************************************************************
main                       : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(venv) ➜  ansible git:(lab5) ✗  ansible-inventory -i inventory/default_yandex.yml  --list     
{
    "_meta": {
        "hostvars": {
            "main": {
                "ansible_host": "51.250.29.149",
                "ansible_user": "wiirtex"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex"
        ]
    },
    "yandex": {
        "hosts": [
            "main"
        ]
    }
}

```