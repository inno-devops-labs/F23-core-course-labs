# Lab 6


## Task 1
1. Create an Ansible Role: Done
2. Update the Playbook: Done
3. Deployment Output:

50 last lines of the deployment command:
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
1. Group Tasks with Blocks: Done
2. Role dependency: done, in `web_app/meta/main.yml`
```
dependencies:
  - role: docker
```
3. Tags: docker-deps, docker-install, docker-compose-install, deploy-app, wipe-app
4. Wipe logic: in tasks/0-wipe.yml: stops container, removes container, removes image, removes files
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
5. Separate tag for wipe: `wipe-app`
6. `docker-compose.yml`: is created from template `web_app/templates/docker-compose.yml.j2`
7. Template delivery: `web_app/templates/docker-compose.yml.j2`
Now the deployment looks like:
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

Also I have parameterized ssh connection and app settings, which are now stored in yml configs within `ansible/vars` directory.


![python_app](https://i.imgur.com/E4IGkdW.png)


## Bonus Task

The structure of playbooks directory is now as follows:
```
$ tree playbooks/
playbooks/
└── dev
    ├── app_go
    │   └── main.yaml
    └── app_python
        └── main.yaml
```

Playbook for the Go app is located in `playbooks/dev/app_go/main.yaml`
Deploy go app (skip Docker dependency, it is already installed by python_app role):

```
$ ansible-playbook -i inventory/yacloud_compute.yaml playbooks/dev/app_go/main.yaml --tags deploy-app

PLAY [all] *****************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************
ok: [terraform-vm]

TASK [web_app : Deploy app (docker-compose version)] ****************************************************************
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

Go app is deployed:

![go app](https://i.imgur.com/MVJdeRw.png)