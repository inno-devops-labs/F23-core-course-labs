# Ansible

## Best practices applied

- Using version control.

- Using tasks with convinient naming.

- Configuration file `ansible.cfg`.

- Using roles.

- Directory layout conventions.

- Using inventory.

- Using defaults to store variables.

- Using tags

- Using blocks

- Using templates

## Task 2 (lab 5)

### Deployment

Command:

`ansible-playbook playbooks/dev/main.yaml --diff`

```
TASK [roles/docker : include_tasks] ************************************************************************************
included: /mnt/c/Users/Damir/Documents/devops-course/ansible/roles/docker/tasks/install_pip.yml for localhost

TASK [roles/docker : Install pip] **************************************************************************************
ok: [localhost]

TASK [roles/docker : include_tasks] ************************************************************************************
included: /mnt/c/Users/Damir/Documents/devops-course/ansible/roles/docker/tasks/install_docker.yml for localhost

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
included: /mnt/c/Users/Damir/Documents/devops-course/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [roles/docker : Install Docker Compose] ***************************************************************************
changed: [localhost]

PLAY RECAP *************************************************************************************************************
localhost                  : ok=11   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory

Command:

`ansible-inventory -i inventory/local_dev_inventory.yml --list`

Output:

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

## Bonus task (lab 5)

- 12 Hours to complete the whole assignment

- Updated terraform AWS : Assigned ssh key to instance to make ssh connection available. No ssh key publication.

- Ubuntu 22.04 LTS Jammy from AWS market place, as I don't want to spend more time for this assignment

### Deployment

Command:

`ansible-playbook main.yaml --diff --key-file ~/.ssh/id_rsa`

Output:

```
PLAY [Prepare docker] ********************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************
The authenticity of host 'ec2-54-213-193-148.us-west-2.compute.amazonaws.com (54.213.193.148)' can't be established.
ED25519 key fingerprint is SHA256:myiRuHfxGG2f4XWrm5K1KaknXmy8HrfLKgO39L8RT60.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Enter passphrase for key '/root/.ssh/id_rsa':
ok: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : include_tasks] ************************************************************************************************************
included: /mnt/c/Users/Damir/Documents/devops-course/ansible/roles/docker/tasks/install_pip.yml for ec2-54-213-193-148.us-west-2.compute.amazonaws.com

TASK [docker : Install pip] **************************************************************************************************************
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
changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : include_tasks] ************************************************************************************************************
included: /mnt/c/Users/Damir/Documents/devops-course/ansible/roles/docker/tasks/install_docker.yml for ec2-54-213-193-148.us-west-2.compute.amazonaws.com

TASK [docker : Update apt cache] *********************************************************************************************************
changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : Install Docker dependencies] **********************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 9 not upgraded.
changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : Add Docker apt key] *******************************************************************************************************
changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : Add Docker repository] ****************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : Install Docker] ***********************************************************************************************************
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
changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

TASK [docker : include_tasks] ************************************************************************************************************
included: /mnt/c/Users/Damir/Documents/devops-course/ansible/roles/docker/tasks/install_compose.yml for ec2-54-213-193-148.us-west-2.compute.amazonaws.com

TASK [docker : Install Docker Compose] ***************************************************************************************************
changed: [ec2-54-213-193-148.us-west-2.compute.amazonaws.com]

PLAY RECAP *******************************************************************************************************************************
ec2-54-213-193-148.us-west-2.compute.amazonaws.com : ok=11   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory

Command:

`ansible-inventory -i inventory/default_aws_ec2.yml --list`

Output:

```
{
    "_meta": {
        "hostvars": {
            "ec2-54-213-193-148.us-west-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2023-10-03T18:23:50+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0448cfd300d8580c6"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "******",
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
                "instance_id": "i-0526d50a055f78cec",
                "instance_type": "t2.nano",
                "key_name": "ssh-key-name",
                "launch_time": "2023-10-03T18:23:49+00:00",
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
                            "public_dns_name": "ec2-54-213-193-148.us-west-2.compute.amazonaws.com",
                            "public_ip": "54.213.193.148"
                        },
                        "attachment": {
                            "attach_time": "2023-10-03T18:23:49+00:00",
                            "attachment_id": "eni-attach-0bb3923fc51ebae26",
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
                        "mac_address": "02:94:c5:f9:2f:87",
                        "network_interface_id": "eni-0b10325a885620a60",
                        "owner_id": "682849823866",
                        "private_dns_name": ******,
                        "private_ip_address": ******,
                        "private_ip_addresses": ******
                        ],
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
                "private_dns_name": "******",
                "private_dns_name_options": ******,
                "private_ip_address": "******",
                "product_codes": [
                    {
                        "product_code_id": "47xbqns9xujfkkjt189a13aqe",
                        "product_code_type": "marketplace"
                    }
                ],
                "public_dns_name": "ec2-54-213-193-148.us-west-2.compute.amazonaws.com",
                "public_ip_address": "54.213.193.148",
                "requester_id": "",
                "reservation_id": "r-06158c310ba29c2b4",
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
                    "Name": "DevOps_Server"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2023-10-03T18:23:49+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0fac2f3aeb84676e4"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws_ec2",
            "tag_Name_DevOps_Server",
            "instance_type_t2_nano",
            "aws_region_us_west_2"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ec2-54-213-193-148.us-west-2.compute.amazonaws.com"
        ]
    },
    "aws_region_us_west_2": {
        "hosts": [
            "ec2-54-213-193-148.us-west-2.compute.amazonaws.com"
        ]
    },
    "instance_type_t2_nano": {
        "hosts": [
            "ec2-54-213-193-148.us-west-2.compute.amazonaws.com"
        ]
    },
    "tag_Name_DevOps_Server": {
        "hosts": [
            "ec2-54-213-193-148.us-west-2.compute.amazonaws.com"
        ]
    }
}
```

---

## Task 1 (lab 6)

Command:

`ansible-playbook playbooks/dev/main.yaml --diff`

```
PLAY [Deploy docker image] *********************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [localhost]

TASK [web_app : Check if container exists] *****************************************************************************
ok: [localhost]

TASK [web_app : Stop the container if it exists] ***********************************************************************
skipping: [localhost]

TASK [web_app : Remove the container if it exists] *********************************************************************
skipping: [localhost]

TASK [web_app : Pull the Docker image] *********************************************************************************
ok: [localhost]

TASK [web_app : Run the Docker container] ******************************************************************************
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

PLAY RECAP *************************************************************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

## Task 2 (lab 6)

I have such structure of role:

```
.
|-- defaults
|   `-- main.yml
|-- meta
|   `-- main.yml
|-- tasks
|   |-- wipe_app.yml
|   |-- stop_app.yml
|   |-- deploy_app.yml
|   `-- main.yml
`-- templates
    `-- docker-compose.yml.j2
```

I used `stop_app` task to stop container (in case when I don't need to wipe). `deploy_app` task is used to deploy docker compose.

### Outputs

Command:

`ansible-playbook playbooks/dev/main.yaml --diff`

```
TASK [web_app : Create directory for my-app] *********************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/my-app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Create directory for Docker Compose] *************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/my-app/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Run Docker Compose by template] ******************************************************************************************
--- before
+++ after: /root/.ansible/tmp/ansible-local-11072cnw01ff9/tmplfypnnrh/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  my-app:
+    image: "nabiull2020/moscow-time-flask-app:latest"
+    container_name: "my-container"
+    ports:
+      - "8000:8000"
+    restart: unless-stopped
\ No newline at end of file

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker Compose] ***************************************************************************************
changed: [localhost]

PLAY RECAP *******************************************************************************************************************************
localhost                  : ok=21   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Bonus task (lab 6)

### Python app

Folder: `ansible/playbooks/app_python`

```
TASK [web_app : Run Docker Compose by template] ******************************************************************************************
--- before
+++ after: /root/.ansible/tmp/ansible-local-157714gw1jz57/tmpgddxgwsm/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  python_app:
+    image: "nabiull2020/moscow-time-flask-app:latest"
+    container_name: "python_app"
+    ports:
+      - "8000:8000"
+    restart: unless-stopped
\ No newline at end of file

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker Compose] ***************************************************************************************
changed: [localhost]

PLAY RECAP *******************************************************************************************************************************
localhost                  : ok=17   changed=4    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0
```

### C# app

Folder: `ansible/playbooks/app_c#`

```
TASK [web_app : Create directory for c_sharp_app] ****************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/c_sharp_app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Create directory for Docker Compose] *************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/c_sharp_app/docker-compose",
-    "state": "absent"
+    "state": "directory"
 }

changed: [localhost]

TASK [web_app : Run Docker Compose by template] ******************************************************************************************
--- before
+++ after: /root/.ansible/tmp/ansible-local-23223jegmezf8/tmpz306p59q/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: '3.8'
+services:
+  c_sharp_app:
+    image: "nabiull2020/programmer-profile-asp-net:latest"
+    container_name: "c_sharp_app"
+    ports:
+      - "8080:80"
+    restart: unless-stopped
\ No newline at end of file

changed: [localhost]

RUNNING HANDLER [web_app : Restart Docker Compose] ***************************************************************************************
changed: [localhost]

PLAY RECAP *******************************************************************************************************************************
localhost                  : ok=20   changed=7    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```