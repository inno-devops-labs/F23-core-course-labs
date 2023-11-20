# Lab 6


## Task 1

```
$ ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml | tail -n 50
[WARNING]: Failed to load inventory plugin, skipping docker_container

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [terraform-vm]

TASK [docker : Install pip] ****************************************************
changed: [terraform-vm]

TASK [docker : Verify pip installation] ****************************************
changed: [terraform-vm]

TASK [docker : pip version] ****************************************************
ok: [terraform-vm] => {
    "msg": "pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)"
}

TASK [docker : Install docker] *************************************************
changed: [terraform-vm]

TASK [docker : Verify docker installation] *************************************
changed: [terraform-vm]

TASK [docker : docker version] *************************************************
ok: [terraform-vm] => {
    "msg": "Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1"
}

TASK [docker : Install docker-compose] *****************************************
changed: [terraform-vm]

TASK [docker : Verify docker-compose installation] *****************************
changed: [terraform-vm]

TASK [docker : docker-compose version] *****************************************
ok: [terraform-vm] => {
    "msg": "docker-compose version 1.29.2, build unknown"
}

TASK [web_app : start python_app container] ************************************
changed: [terraform-vm]

PLAY RECAP *********************************************************************
terraform-vm               : ok=11   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Task 2

```
dependencies:
  - role: docker
```

```
$ ansible-playbook -e 'web_app_full_wipe=true' -i inventory/yacloud_compute.yaml playbooks/dev/main.yaml --tags wipe-app

PLAY [all] *********************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************
ok: [terraform-vm]

TASK [web_app : Wipe app] ***********************************************************************************
included: /home/artem/iu/devops/core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for terraform-vm

TASK [web_app : Stop app container] *************************************************************************
changed: [terraform-vm]

TASK [web_app : Remove app container] ***********************************************************************
changed: [terraform-vm]

TASK [web_app : Remove app image] ***************************************************************************
changed: [terraform-vm]

PLAY RECAP *********************************************************************************************************
terraform-vm               : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```
$ ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/app_go/main.yaml --tags deploy-app

PLAY [all] *****************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Deploy app (docker-compose version)] ***********************************************************************
included: /home/artem/iu/devops/core-course-labs/ansible/roles/web_app/tasks/1-app-deploy.yml for terraform-vm

TASK [web_app : Create app directory] **************************************************************************************
changed: [terraform-vm]

TASK [web_app : Deliver compose file to target server] *********************************************************************
changed: [terraform-vm]

TASK [web_app : Start docker-compose service] ******************************************************************************
changed: [terraform-vm]

PLAY RECAP *****************************************************************************************************************
terraform-vm               : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```