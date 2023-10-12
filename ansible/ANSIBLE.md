# ANSIBLE


### playbook:
```
$ ansible-playbook playbooks/main.yml --diff

[WARNING]: Invalid characters were found in group names but not replaced, use -vvvv to see details

PLAY [Deploy web application on Yandex Cloud Virtual Machine] ***************************************************************

TASK [Gathering Facts] ******************************************************************************************************
ok: [devopsuser@51.250.30.128]

TASK [docker : Add Docker GPG key] ******************************************************************************************
ok: [devopsuser@51.250.30.128]

TASK [docker : Add Docker APT repository] ***********************************************************************************
ok: [devopsuser@51.250.30.128]

TASK [docker : Update package index files] **********************************************************************************
changed: [devopsuser@51.250.30.128]

TASK [docker : Install latest Docker CE] ************************************************************************************
ok: [devopsuser@51.250.30.128]

TASK [docker : Install Python3 and pip3] ************************************************************************************
ok: [devopsuser@51.250.30.128]

TASK [docker : Install Docker compose] **************************************************************************************
ok: [devopsuser@51.250.30.128]

TASK [web_app : Run app_python:latest] **************************************************************************************
ok: [devopsuser@51.250.30.128]

PLAY RECAP ******************************************************************************************************************
devopsuser@51.250.30.128   : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

### inventory:
```
$ ansible-inventory -i inventory/inventory.ini --list

[WARNING]: Invalid characters were found in group names but not replaced, use -vvvv to see details
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped",
            "yandex-cloud"
        ]
    },
    "yandex-cloud": {
        "hosts": [
            "devopsuser@51.250.30.128"
        ]
    }
}

```