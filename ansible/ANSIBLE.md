# Docker role

## Setup
Installing requirements:
```
python >= 3.6

boto3 >= 1.22.0

botocore >= 1.25.0
```

## ansible-playbook playbooks/dev/main.yml --diff

```
PLAY [Prepare docker] ***************************************************************************************************************************************************************************************************************************************
TASK [Gathering Facts] **************************************************************************************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [docker : Execute apt update] **************************************************************************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.pip : Ensure Pip is installed.] ***********************************************************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.pip : Ensure pip_install_packages are installed.] *****************************************************************************************************************************************************************************************changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com] => (item={'name': 'docker'})
changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com] => (item={'name': 'docker-compose'})

TASK [geerlingguy.docker : Load OS-specific vars.] **********************************************************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************************************************************************************************************included: /home/nikolina2k/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for ec2-35-93-48-64.us-west-2.compute.amazonaws.com

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ********************************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure dependencies are installed.] **********************************************************************************************************************************************************************************************changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *****************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key.] *************************************************************************************************************************************************************************************************************changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *****************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Add Docker repository.] **********************************************************************************************************************************************************************************************************changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages.] ********************************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ********************************************************************************************************************************************************************************changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose plugin.] **************************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] *******************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Configure Docker daemon options.] ************************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***********************************************************************************************************************************************************************************ok: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] *******************************************************************************************************************************************************************
RUNNING HANDLER [geerlingguy.docker : restart docker] *******************************************************************************************************************************************************************************************************changed: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Get docker group info using getent.] *********************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

TASK [geerlingguy.docker : include_tasks] *******************************************************************************************************************************************************************************************************************skipping: [ec2-35-93-48-64.us-west-2.compute.amazonaws.com]

PLAY RECAP **************************************************************************************************************************************************************************************************************************************************ec2-35-93-48-64.us-west-2.compute.amazonaws.com : ok=14   changed=6    unreachable=0    failed=0    skipped=13   rescued=0    ignored=0
```

## ansible-inventory -i default_aws_ec2.yml --list

```
{
    "_meta": {
        "hostvars": {
            "ec2-35-93-48-64.us-west-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2023-10-02T18:29:48+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-090db306bb89619f9"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "terraform-20231002182947544700000001",
                "cpu_options": {
                    "core_count": 1,
                    "threads_per_core": 1
                },
                "current_instance_boot_mode": "legacy-bios",
                "ebs_optimized": false,
                "enclave_options": {
                    "enabled": false
                },
                "hibernation_options": {
                    "configured": false
                },
                "hypervisor": "xen",
                "iam_instance_profile": {
                    "arn": "arn:aws:iam::580563234576:instance-profile/AdminAccess",
                    "id": "AIPAYOLCD54IHYPTAKNRH"
                },
                "image_id": "ami-830c94e3",
                "instance_id": "i-0a017d4fe65ad7e7f",
                "instance_type": "t2.micro",
                "launch_time": "2023-10-02T18:29:47+00:00",
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
                            "public_dns_name": "ec2-35-93-48-64.us-west-2.compute.amazonaws.com",
                            "public_ip": "35.93.48.64"
                        },
                        "attachment": {
                            "attach_time": "2023-10-02T18:29:47+00:00",
                            "attachment_id": "eni-attach-0c5091c8e4eb633fb",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-02c53912ed412ff55",
                                "group_name": "default"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "<<SECRET_HIDDEN!!!>>",
                        "network_interface_id": "eni-0eb0e9dec10c6ebda",
                        "owner_id": "580563234576",
                        "private_dns_name": "<<SECRET_HIDDEN!!!>>",
                        "private_ip_address": "<<SECRET_HIDDEN!!!>>",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-35-93-48-64.us-west-2.compute.amazonaws.com",
                                    "public_ip": "35.93.48.64"
                                },
                                "primary": true,
                                "private_dns_name": "<<SECRET_HIDDEN!!!>>",
                                "private_ip_address": "<<SECRET_HIDDEN!!!>>"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0b999c5d212d7762f",
                        "vpc_id": "vpc-00bdc581d5263daec"
                    }
                ],
                "owner_id": "580563234576",
                "placement": {
                    "availability_zone": "us-west-2b",
                    "group_name": "",
                    "region": "us-west-2",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "<<SECRET_HIDDEN!!!>>",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": false,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "<<SECRET_HIDDEN!!!>>",
                "product_codes": [],
                "public_dns_name": "ec2-35-93-48-64.us-west-2.compute.amazonaws.com",
                "public_ip_address": "35.93.48.64",
                "requester_id": "",
                "reservation_id": "r-0c3c6f3a893a89151",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-02c53912ed412ff55",
                        "group_name": "default"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0b999c5d212d7762f",
                "tags": {
                    "Name": "ExampleAppServerInstance"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2023-10-02T18:29:47+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-00bdc581d5263daec"
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
            "ec2-35-93-48-64.us-west-2.compute.amazonaws.com"
        ]
    }
}
```
