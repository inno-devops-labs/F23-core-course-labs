# Ansible 1

## Playbook
`ansible-playbook playbooks/dev/main.yaml --diff`

```
TASK [roles/docker : include_tasks] ************************************************************************************
included: /home/parallels/Desktop/Parallels Shared Folders/Home/Desktop/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for localhost
TASK [roles/docker : Install pip] **************************************************************************************
ok: [localhost]
TASK [roles/docker : include_tasks] ************************************************************************************
included: /home/parallels/Desktop/Parallels Shared Folders/Home/Desktop/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost
TASK [roles/docker : Update cache] *********************************************************************************
ok: [localhost]
TASK [roles/docker : Install dependencies] **********************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 48 not upgraded.
changed: [localhost]
TASK [roles/docker : Add apt key] *******************************************************************************
changed: [localhost]
TASK [roles/docker : Add repository] ****************************************************************************
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
included: /home/parallels/Desktop/Parallels Shared Folders/Home/Desktop/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost
TASK [roles/docker : Install Compose] ***************************************************************************
changed: [localhost]
PLAY RECAP *************************************************************************************************************
localhost                  : ok=11   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory

`ansible-inventory -i inventory/dev_inventory.yml --list`

```
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

## Bonus

## Playbook

`ansible-playbook playbooks/dev/main.yaml --diff --key-file ~/.ssh/id_rsa`

```
PLAY [Prepare docker] **************************************************************************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************************************************************************
The authenticity of host 'ec2-34-216-206-103.us-west-2.compute.amazonaws.com (34.216.206.103)' can't be established.
ED25519 key fingerprint is SHA256:NEwsA7AGknW/y5fbxsJe1dtZiXeTMRLKDB8RtcV11S0.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************************************************************************
included: /Users/ann_d/Desktop/core-course-labs/ansible/roles/docker/tasks/install_pip.yml for ec2-34-216-206-103.us-west-2.compute.amazonaws.com

TASK [docker : Install pip] ********************************************************************************************************************************************************************************
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-wheel python3.10-dev rpcsvc-proto
  zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 9 not upgraded.
changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************************************************************************
included: /Users/ann_d/Desktop/core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ec2-34-216-206-103.us-west-2.compute.amazonaws.com

TASK [docker : Update cache] *******************************************************************************************************************************************************************************
changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : Install dependencies] ***********************************************************************************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 9 not upgraded.
changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : Add apt key] ********************************************************************************************************************************************************************************
changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : Add repository] *****************************************************************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : Install Docker] *****************************************************************************************************************************************************************************
The following additional packages will be installed:
  docker-buildx-plugin docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 9 not upgraded.
changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

TASK [docker : include_tasks] ******************************************************************************************************************************************************************************
included: /Users/ann_d/Desktop/core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ec2-34-216-206-103.us-west-2.compute.amazonaws.com

TASK [docker : Install Compose] ****************************************************************************************************************************************************************************
changed: [ec2-34-216-206-103.us-west-2.compute.amazonaws.com]

PLAY RECAP *************************************************************************************************************************************************************************************************
ec2-34-216-206-103.us-west-2.compute.amazonaws.com : ok=11   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
## Inventory

`ansible-inventory -i inventory/default_aws_ec2.yml --list`

```
{
    "_meta": {
        "hostvars": {
            "ec2-34-216-206-103.us-west-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2023-10-03T19:11:40+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0c9d71a6602148b2d"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "-",
                "cpu_options": {
                    "core_count": 1,
                    "threads_per_core": 1
                },
                "current_instance_boot_mode": "legacy-bios",
                "ebs_optimized": false,
                "ena_support": true,
                "enclave_options": {
                    "enabled": false
                },
                "hibernation_options": {
                    "configured": false
                },
                "hypervisor": "xen",
                "image_id": "ami-0640ee265e4ae17ea",
                "instance_id": "i-09c78ce1d266ae301",
                "instance_type": "t2.nano",
                "key_name": "ssh-key",
                "launch_time": "2023-10-03T19:11:39+00:00",
                "maintenance_options": {
                    "auto_recovery": "default"
                },
                "metadata_options": {
                    "http_endpoint": "enabled",
                    "http_protocol_ipv6": "disabled",
                    "http_put_response_hop_limit": 1,
                    "http_tokens": "optional",
                    "instance_metadata_tags": "disabled",
                    "state": "applied"
                },
                "monitoring": {
                    "state": "disabled"
                },
                "network_interfaces": [
                    {
                        "association": {
                            "ip_owner_id": "amazon",
                            "public_dns_name": "ec2-34-216-206-103.us-west-2.compute.amazonaws.com",
                            "public_ip": "34.216.206.103"
                        },
                        "attachment": {
                            "attach_time": "2023-10-03T19:11:39+00:00",
                            "attachment_id": "eni-attach-0b9c4ca916f583fa5",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0ba46fa84cd286e3e",
                                "group_name": "default"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:69:b9:28:45:fb",
                        "network_interface_id": "eni-0be4e627ccd5461bd",
                        "owner_id": "682849823866",
                        "private_dns_name": "-",
                        "private_ip_address": "-",
                        "private_ip_addresses": "-",
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0aab25821e22bed79",
                        "vpc_id": "vpc-0fac2f3aeb84676e4"
                    }
                ],
                "owner_id": "682849823866",
                "placement": {
                    "availability_zone": "us-west-2a",
                    "group_name": "",
                    "region": "us-west-2",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "-",
                "private_dns_name_options": "-",
                "private_ip_address": "-",
                "product_codes": [
                    {
                        "product_code_id": "47xbqns9xujfkkjt189a13aqe",
                        "product_code_type": "marketplace"
                    }
                ],
                "public_dns_name": "ec2-34-216-206-103.us-west-2.compute.amazonaws.com",
                "public_ip_address": "34.216.206.103",
                "requester_id": "",
                "reservation_id": "r-00ad07bb99a1f708f",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0ba46fa84cd286e3e",
                        "group_name": "default"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0aab25821e22bed79",
                "tags": {
                    "Name": "annadlu_server_2"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2023-10-03T19:11:39+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0fac2f3aeb84676e4"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws_ec2",
            "tag_Name_annadlu_server_2",
            "instance_type_t2_nano",
            "aws_region_us_west_2"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ec2-34-216-206-103.us-west-2.compute.amazonaws.com"
        ]
    },
    "aws_region_us_west_2": {
        "hosts": [
            "ec2-34-216-206-103.us-west-2.compute.amazonaws.com"
        ]
    },
    "instance_type_t2_nano": {
        "hosts": [
            "ec2-34-216-206-103.us-west-2.compute.amazonaws.com"
        ]
    },
    "tag_Name_annadlu_server_2": {
        "hosts": [
            "ec2-34-216-206-103.us-west-2.compute.amazonaws.com"
        ]
    }
}
```

# Ansible 2

## Task 1
## Playbook
`ansible-playbook playbooks/dev/main.yaml --diff`
```
PLAY [Deploy image] ************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [web_app : Check if container exists] *************************************
ok: [localhost]

TASK [web_app : Stop the container if it exists] *******************************
skipping: [localhost]

TASK [web_app : Remove the container if it exists] *****************************
skipping: [localhost]

TASK [web_app : Pull the Docker image] *****************************************
changed: [localhost]

TASK [web_app : Run the Docker container] **************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=2    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

## Task 2
.
|-- defaults
|   `-- main.yml
|-- meta
|   `-- main.yml
|-- tasks
|   |-- app_wipe.yml
|   |-- app_stop.yml
|   |-- app_deploy.yml
|   `-- main.yml
`-- templates
   `-- docker-compose.yml.j2

`ansible-inventory -i inventory/default_aws_ec2.yml --list`

```
PLAY [Deploy image] ************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [web_app : Check if Docker Compose exists] ********************************
skipping: [localhost]

TASK [web_app : Stop Docker Compose if it exists] ******************************
skipping: [localhost]

TASK [web_app : Check if directory /Users/ann_d/Desktop/app_python exists] *****
ok: [localhost]

TASK [web_app : Check if Docker Compose exists] ********************************
ok: [localhost]

TASK [web_app : Remove Docker Compose containers if exists] ********************
skipping: [localhost]

TASK [web_app : Remove Docker Compose files if they exist] *********************
skipping: [localhost]

TASK [web_app : Remove app directory /Users/ann_d/Desktop/app_python] **********
skipping: [localhost]

TASK [web_app : Create directory for app_python] *******************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Create directory for Docker Compose] ***************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_python/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Run Docker Compose by template] ********************************
--- before
+++ after: /Users/ann_d/.ansible/tmp/ansible-local-66969wd7akmj9/tmphq_3f09k/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  app_python:
+    image: "annadluzhinskaya/python-moscow-time:latest"
+    container_name: "app-container"
+    ports:
+      - "8000:8080"
+    restart: unless-stopped

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker] *************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=7    changed=4    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
```

## Bonus task
### Python

```
PLAY [Deploy python app in docker] *********************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [web_app : Check if directory /Users/ann_d/Desktop/app_python exists] *****
ok: [localhost]

TASK [web_app : Check if Docker Compose exists] ********************************
ok: [localhost]

TASK [web_app : Remove Docker Compose containers if exists] ********************
changed: [localhost]

TASK [web_app : Remove Docker Compose files if they exist] *********************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_python/docker-compose",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/Users/ann_d/Desktop/app_python/docker-compose/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [localhost]

TASK [web_app : Remove app directory /Users/ann_d/Desktop/app_python] **********
--- before
+++ after
@@ -1,8 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_python",
-    "path_content": {
-        "directories": [],
-        "files": []
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [localhost]

TASK [web_app : Create directory for app_python] *******************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Create directory for Docker Compose] ***************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_python/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Run Docker Compose by template] ********************************
--- before
+++ after: /Users/ann_d/.ansible/tmp/ansible-local-6906979iol37q/tmpuylvdzzf/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  app_python:
+    image: "annadluzhinskaya/python-moscow-time:latest"
+    container_name: "app_python"
+    ports:
+      - "8000:8080"
+    restart: unless-stopped

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker] *************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

### C#
```
PLAY [Deploy c# app in docker] ********************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************
ok: [localhost]

TASK [web_app : Check if directory /Users/ann_d/Desktop/app_c_sharp exists] ***********************************************************
ok: [localhost]

TASK [web_app : Check if Docker Compose exists] ***************************************************************************************
ok: [localhost]

TASK [web_app : Remove Docker Compose containers if exists] ***************************************************************************
skipping: [localhost]

TASK [web_app : Remove Docker Compose files if they exist] ****************************************************************************
skipping: [localhost]

TASK [web_app : Remove app directory /Users/ann_d/Desktop/app_c_sharp] ****************************************************************
skipping: [localhost]

TASK [web_app : Create directory for app_c_sharp] *************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_c_sharp",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Create directory for Docker Compose] **********************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/Users/ann_d/Desktop/app_c_sharp/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Run Docker Compose by template] ***************************************************************************************
--- before
+++ after: /Users/ann_d/.ansible/tmp/ansible-local-69366rrzhic1t/tmprxy71ad2/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  app_c_sharp:
+    image: "annadluzhinskaya/pet-app:latest"
+    container_name: "app_c_sharp"
+    ports:
+      - "8088:80"
+    restart: unless-stopped

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker] ********************************************************************************************
changed: [localhost]

PLAY RECAP ****************************************************************************************************************************
localhost                  : ok=7    changed=4    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0 
```
