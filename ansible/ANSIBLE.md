# ANSIBLE


### Outputs


```
$ ansible-playbook -i inventory/dev.ini ./playbooks/app_python/main.yml --tags "app-deploy,app-start"
[WARNING]: Invalid characters were found in group names but not replaced, use -vvvv to see details

PLAY [Deploy web application on Yandex Cloud Virtual Machine] ************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************
ok: [web_app]

TASK [web_app : include_tasks] *******************************************************************************************************************
included: /home/aibek/iu/devops/ansible/roles/web_app/tasks/deploy.yml for web_app

TASK [web_app : Create web_app directory] ********************************************************************************************************
ok: [web_app]

TASK [web_app : Copy docker-compose.yml from the template] ***************************************************************************************
ok: [web_app]

TASK [web_app : Run docker-compose] **************************************************************************************************************
ok: [web_app]

PLAY RECAP ***************************************************************************************************************************************
web_app                    : ok=5    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
