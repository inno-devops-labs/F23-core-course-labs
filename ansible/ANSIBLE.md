# Ansible-related work

 ### Deployment

 ```zsh
 $ ansible-playbook playbooks/dev/main.yaml --diff
 ...
 
 TASK [roles/docker : include_tasks] ************************************************************************************
 included: /Users/dinar/devops-course/ansible/roles/docker/tasks/install_pip.yml for localhost

 TASK [roles/docker : Install pip] **************************************************************************************
 ok: [localhost]

 TASK [roles/docker : include_tasks] ************************************************************************************
 included: /Users/dinar/devops-course/ansible/roles/docker/tasks/install_docker.yml for localhost

 TASK [roles/docker : Update apt cache] *********************************************************************************
 ok: [localhost]

 TASK [roles/docker : Install Docker dependencies] **********************************************************************
The following NEW packages will be installed:
   apt-transport-https
 0 upgraded, 1 newly installed, 0 to remove and 48 not upgraded.
 changed: [localhost]

 TASK [roles/docker : Add Docker apt key] *******************************************************************************
 changed: [localhost]

 TASK [roles/docker : Add Docker repository] ****************************************************************************
 --- before: /dev/null
 +++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
 @@ -0,0 +1 @@
 +deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

 changed: [localhost]

 TASK [roles/docker : Install Docker] ***********************************************************************************
 The following additional packages will be installed:
   dbus-user-session docker-buildx-plugin docker-compose-plugin libltdl7
   libslirp0 pigz slirp4netns
 Suggested packages:
   aufs-tools cgroupfs-mount | cgroup-lite
 The following NEW packages will be installed:
   containerd.io dbus-user-session docker-buildx-plugin docker-ce docker-ce-cli
   docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
   slirp4netns
 0 upgraded, 11 newly installed, 0 to remove and 48 not upgraded.
 changed: [localhost]

 TASK [roles/docker : include_tasks] ************************************************************************************
 included: /Users/dinar/devops-course/ansible/roles/docker/tasks/install_compose.yml for localhost

 TASK [roles/docker : Install Docker Compose] ***************************************************************************
 changed: [localhost]

 PLAY RECAP *************************************************************************************************************
localhost                  : ok=11   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

 ### Inventory 

 ```zsh
 $ ansible-inventory -i inventory/inventory_local.yml --list
 {
     "_meta": {
         "hostvars": {
             "localhost": {
                 "ansible_connection": "local"
             }
         }
     },
     "all": {
         "children": [
             "ungrouped",
             "devhost"
         ]
     },
     "devhost": {
         "hosts": [
             "localhost"
         ]
     }
 }
 ```