## ansible-playbook playbooks/dev/main.yml --diff

```
PLAY [Prepare docker] ***************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************
ok: [localhost]

TASK [docker : Execute apt update] **************************************************************************************************************************
changed: [localhost]

TASK [geerlingguy.pip : Ensure Pip is installed.] ***********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] *****************************************************************************************
changed: [localhost] => (item={'name': 'docker'})
changed: [localhost] => (item={'name': 'docker-compose'})

TASK [geerlingguy.docker : Load OS-specific vars.] **********************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************
included: /home/shohjahon/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for localhost

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ********************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **********************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *****************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Add Docker apt key.] *************************************************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *****************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Add Docker repository.] **********************************************************************************************************
changed: [localhost]

TASK [geerlingguy.docker : Install Docker packages.] ********************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ********************************************************************************
The following additional packages will be installed:
  dbus-user-session docker-buildx-plugin docker-compose-plugin libltdl7
  libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io dbus-user-session docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 11 newly installed, 0 to remove and 165 not upgraded.
changed: [localhost]

TASK [geerlingguy.docker : Install docker-compose plugin.] **************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *******************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Configure Docker daemon options.] ************************************************************************************************
skipping: [localhost]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***********************************************************************************
ok: [localhost]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *******************************************************************
skipping: [localhost]

PLAY RECAP **************************************************************************************************************************************************localhost                  : ok=14   changed=5    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0

```


## ansible-inventory -i inventory/default.yml --list

```
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "localhost"
        ]
    }
}
```



## Bonus Task: Dynamic Inventory:

After implementing dynamic inventory:

### ansible-inventory -i inventory/default_aws_ec2.yml --list

```
{
    "_meta": {
        "hostvars": {
            "ec2-35-86-141-140.us-west-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2023-09-26T11:10:06+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0e2847d530fa97dc9"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "terraform-20230926111003724600000001",
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
                "iam_instance_profile": {
                    "arn": "arn:aws:iam::150479635815:instance-profile/AdminAccess",
                    "id": "AIPASGCKJAVTXR2LC7NLL"
                },
                "image_id": "ami-08d70e59c07c61a3a",
                "instance_id": "i-0b404948e8227d7e6",
                "instance_type": "t2.micro",
                "launch_time": "2023-09-26T11:10:05+00:00",
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
                            "public_dns_name": "ec2-35-86-141-140.us-west-2.compute.amazonaws.com",
                            "public_ip": "35.86.141.140"
                        },
                        "attachment": {
                            "attach_time": "2023-09-26T11:10:05+00:00",
                            "attachment_id": "eni-attach-05a18ee4d88801ad0",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-073bb22849dea28f7",
                                "group_name": "default"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:01:21:27:74:e7",
                        "network_interface_id": "eni-036be9c6dc73ee098",
                        "owner_id": "150479635815",
                        "private_dns_name": "<<<HIDDEN!>>>",
                        "private_ip_address": "<<<HIDDEN!>>>",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-35-86-141-140.us-west-2.compute.amazonaws.com",
                                    "public_ip": "35.86.141.140"
                                },
                                "primary": true,
                                "private_dns_name": "<<<HIDDEN!>>>",
                                "private_ip_address": "<<<HIDDEN!>>>"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0fffe2b4595171c0b",
                        "vpc_id": "vpc-09aed16b569ae45c1"
                    }
                ],
                "owner_id": "150479635815",
                "placement": {
                    "availability_zone": "us-west-2b",
                    "group_name": "",
                    "region": "us-west-2",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "<<<HIDDEN!>>>",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": false,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "<<<HIDDEN!>>>",
                "product_codes": [],
                "public_dns_name": "ec2-35-86-141-140.us-west-2.compute.amazonaws.com",
                "public_ip_address": "35.86.141.140",
                "requester_id": "",
                "reservation_id": "r-03762a7fa4b437275",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-073bb22849dea28f7",
                        "group_name": "default"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0fffe2b4595171c0b",
                "tags": {
                    "Name": "ExampleAppServerInstance"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2023-09-26T11:10:05+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-09aed16b569ae45c1"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws_ec2"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ec2-35-86-141-140.us-west-2.compute.amazonaws.com"
        ]
    }
}
```
