

- [ ] Add meta dependencies


## 3.  Deployment Output
```
TF_STATE=../terraform/yandex/ ansible-playbook --inventory-file=/usr/bin/terraform-inventory  --diff playbooks/dev/main.yml | sed -E 's/([0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,7})/XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX/g' | sed -e 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/X.X.X.X/g'


PLAY [vm_1] ********************************************************************

TASK [docker : Ensure that conflicting Docker versions are absent] *************
ok: [X.X.X.X]

TASK [docker : Install Docker] *************************************************
ok: [X.X.X.X]

TASK [docker : Install docker-compose package] *********************************
ok: [X.X.X.X]

PLAY RECAP *********************************************************************
X.X.X.X              : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


## 4. Inventory Details


```json
which terraform-inventory || ./scripts/install_terraform_inventory.sh
/usr/bin/terraform-inventory
TF_STATE=../terraform/yandex/ ansible-inventory --list --inventory-file=/usr/bin/terraform-inventory | sed -E 's/([0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){1,7})/XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX/g' | sed -e 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/X.X.X.X/g'
{
    "_meta": {
        "hostvars": {
            "X.X.X.X": {
                "allow_recreate": "<error>",
                "allow_stopping_for_update": "<error>",
                "ansible_all_ipv4_addresses": [
                    {
                        "__ansible_unsafe": "X.X.X.X"
                    }
                ],
                "ansible_all_ipv6_addresses": [
                    {
                        "__ansible_unsafe": "fe80::XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                    }
                ],
                "ansible_apparmor": {
                    "status": {
                        "__ansible_unsafe": "enabled"
                    }
                },
                "ansible_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_bios_date": {
                    "__ansible_unsafe": "04/01/2014"
                },
                "ansible_bios_vendor": {
                    "__ansible_unsafe": "SeaBIOS"
                },
                "ansible_bios_version": {
                    "__ansible_unsafe": "1.16.1-1"
                },
                "ansible_board_asset_tag": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_board_name": {
                    "__ansible_unsafe": "xeon-e5-2660"
                },
                "ansible_board_serial": {
                    "__ansible_unsafe": "YC-epdp5uqbf5e36dpsf45h"
                },
                "ansible_board_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_board_version": {
                    "__ansible_unsafe": "pc-q35-yc-2.12"
                },
                "ansible_chassis_asset_tag": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_chassis_serial": {
                    "__ansible_unsafe": "xeon-e5-2660"
                },
                "ansible_chassis_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_chassis_version": {
                    "__ansible_unsafe": "xeon-e5-2660"
                },
                "ansible_cmdline": {
                    "BOOT_IMAGE": {
                        "__ansible_unsafe": "/boot/vmlinuz-5.15.0-79-generic"
                    },
                    "biosdevname": {
                        "__ansible_unsafe": "0"
                    },
                    "console": {
                        "__ansible_unsafe": "ttyS0"
                    },
                    "net.ifnames": {
                        "__ansible_unsafe": "0"
                    },
                    "ro": true,
                    "root": {
                        "__ansible_unsafe": "UUID=ed465c6e-049a-41c6-8e0b-c8da348a3577"
                    }
                },
                "ansible_date_time": {
                    "date": {
                        "__ansible_unsafe": "2023-10-03"
                    },
                    "day": {
                        "__ansible_unsafe": "03"
                    },
                    "epoch": {
                        "__ansible_unsafe": "1696370647"
                    },
                    "hour": {
                        "__ansible_unsafe": "22"
                    },
                    "iso8601": {
                        "__ansible_unsafe": "2023-10-03TXXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXXZ"
                    },
                    "iso8601_basic": {
                        "__ansible_unsafe": "20231003T220407981977"
                    },
                    "iso8601_basic_short": {
                        "__ansible_unsafe": "20231003T220407"
                    },
                    "iso8601_micro": {
                        "__ansible_unsafe": "2023-10-03TXXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX.981977Z"
                    },
                    "minute": {
                        "__ansible_unsafe": "04"
                    },
                    "month": {
                        "__ansible_unsafe": "10"
                    },
                    "second": {
                        "__ansible_unsafe": "07"
                    },
                    "time": {
                        "__ansible_unsafe": "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                    },
                    "tz": {
                        "__ansible_unsafe": "UTC"
                    },
                    "tz_offset": {
                        "__ansible_unsafe": "+0000"
                    },
                    "weekday": {
                        "__ansible_unsafe": "Tuesday"
                    },
                    "weekday_number": {
                        "__ansible_unsafe": "2"
                    },
                    "weeknumber": {
                        "__ansible_unsafe": "40"
                    },
                    "year": {
                        "__ansible_unsafe": "2023"
                    }
                },
                "ansible_default_ipv4": {
                    "address": {
                        "__ansible_unsafe": "X.X.X.X"
                    },
                    "alias": {
                        "__ansible_unsafe": "eth0"
                    },
                    "broadcast": {
                        "__ansible_unsafe": ""
                    },
                    "gateway": {
                        "__ansible_unsafe": "X.X.X.X"
                    },
                    "interface": {
                        "__ansible_unsafe": "eth0"
                    },
                    "macaddress": {
                        "__ansible_unsafe": "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                    },
                    "mtu": 1500,
                    "netmask": {
                        "__ansible_unsafe": "X.X.X.X"
                    },
                    "network": {
                        "__ansible_unsafe": "X.X.X.X"
                    },
                    "type": {
                        "__ansible_unsafe": "ether"
                    }
                },
                "ansible_default_ipv6": {},
                "ansible_device_links": {
                    "ids": {
                        "vda": [
                            {
                                "__ansible_unsafe": "virtio-epdpdq9nilnnofbtb58s"
                            }
                        ],
                        "vda1": [
                            {
                                "__ansible_unsafe": "virtio-epdpdq9nilnnofbtb58s-part1"
                            }
                        ],
                        "vda2": [
                            {
                                "__ansible_unsafe": "virtio-epdpdq9nilnnofbtb58s-part2"
                            }
                        ]
                    },
                    "labels": {},
                    "masters": {},
                    "uuids": {
                        "vda2": [
                            {
                                "__ansible_unsafe": "ed465c6e-049a-41c6-8e0b-c8da348a3577"
                            }
                        ]
                    }
                },
                "ansible_devices": {
                    "loop0": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "129600"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "63.28 MB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop1": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "229272"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "111.95 MB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop2": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "102072"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "49.84 MB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop3": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "83648"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "40.84 MB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop4": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "129976"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "63.46 MB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "4096"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop5": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "0"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop6": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "0"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "loop7": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": ""
                        },
                        "links": {
                            "ids": [],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {},
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "0"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "0.00 Bytes"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "0"
                        },
                        "vendor": null,
                        "virtual": 1
                    },
                    "vda": {
                        "holders": [],
                        "host": {
                            "__ansible_unsafe": "SCSI storage controller: Red Hat, Inc. Virtio block device"
                        },
                        "links": {
                            "ids": [
                                {
                                    "__ansible_unsafe": "virtio-epdpdq9nilnnofbtb58s"
                                }
                            ],
                            "labels": [],
                            "masters": [],
                            "uuids": []
                        },
                        "model": null,
                        "partitions": {
                            "vda1": {
                                "holders": [],
                                "links": {
                                    "ids": [
                                        {
                                            "__ansible_unsafe": "virtio-epdpdq9nilnnofbtb58s-part1"
                                        }
                                    ],
                                    "labels": [],
                                    "masters": [],
                                    "uuids": []
                                },
                                "sectors": {
                                    "__ansible_unsafe": "2048"
                                },
                                "sectorsize": 512,
                                "size": {
                                    "__ansible_unsafe": "1.00 MB"
                                },
                                "start": {
                                    "__ansible_unsafe": "2048"
                                },
                                "uuid": null
                            },
                            "vda2": {
                                "holders": [],
                                "links": {
                                    "ids": [
                                        {
                                            "__ansible_unsafe": "virtio-epdpdq9nilnnofbtb58s-part2"
                                        }
                                    ],
                                    "labels": [],
                                    "masters": [],
                                    "uuids": [
                                        {
                                            "__ansible_unsafe": "ed465c6e-049a-41c6-8e0b-c8da348a3577"
                                        }
                                    ]
                                },
                                "sectors": {
                                    "__ansible_unsafe": "16773087"
                                },
                                "sectorsize": 512,
                                "size": {
                                    "__ansible_unsafe": "8.00 GB"
                                },
                                "start": {
                                    "__ansible_unsafe": "4096"
                                },
                                "uuid": {
                                    "__ansible_unsafe": "ed465c6e-049a-41c6-8e0b-c8da348a3577"
                                }
                            }
                        },
                        "removable": {
                            "__ansible_unsafe": "0"
                        },
                        "rotational": {
                            "__ansible_unsafe": "1"
                        },
                        "sas_address": null,
                        "sas_device_handle": null,
                        "scheduler_mode": {
                            "__ansible_unsafe": "none"
                        },
                        "sectors": {
                            "__ansible_unsafe": "16777216"
                        },
                        "sectorsize": {
                            "__ansible_unsafe": "512"
                        },
                        "size": {
                            "__ansible_unsafe": "8.00 GB"
                        },
                        "support_discard": {
                            "__ansible_unsafe": "0"
                        },
                        "vendor": {
                            "__ansible_unsafe": "0x1af4"
                        },
                        "virtual": 1
                    }
                },
                "ansible_distribution": {
                    "__ansible_unsafe": "Ubuntu"
                },
                "ansible_distribution_file_parsed": true,
                "ansible_distribution_file_path": {
                    "__ansible_unsafe": "/etc/os-release"
                },
                "ansible_distribution_file_variety": {
                    "__ansible_unsafe": "Debian"
                },
                "ansible_distribution_major_version": {
                    "__ansible_unsafe": "22"
                },
                "ansible_distribution_release": {
                    "__ansible_unsafe": "jammy"
                },
                "ansible_distribution_version": {
                    "__ansible_unsafe": "22.04"
                },
                "ansible_dns": {
                    "nameservers": [
                        {
                            "__ansible_unsafe": "X.X.X.X"
                        }
                    ],
                    "options": {
                        "edns0": true,
                        "trust-ad": true
                    },
                    "search": [
                        {
                            "__ansible_unsafe": "auto.internal"
                        },
                        {
                            "__ansible_unsafe": "ru-central1.internal"
                        }
                    ]
                },
                "ansible_domain": {
                    "__ansible_unsafe": "auto.internal"
                },
                "ansible_effective_group_id": 0,
                "ansible_effective_user_id": 0,
                "ansible_env": {
                    "HOME": {
                        "__ansible_unsafe": "/root"
                    },
                    "LANG": {
                        "__ansible_unsafe": "C"
                    },
                    "LC_ADDRESS": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_ALL": {
                        "__ansible_unsafe": "C"
                    },
                    "LC_IDENTIFICATION": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_MEASUREMENT": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_MESSAGES": {
                        "__ansible_unsafe": "C"
                    },
                    "LC_MONETARY": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_NAME": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_NUMERIC": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_PAPER": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LC_TELEPHONE": {
                        "__ansible_unsafe": "ru_RU.UTF-8"
                    },
                    "LOGNAME": {
                        "__ansible_unsafe": "root"
                    },
                    "MAIL": {
                        "__ansible_unsafe": "/var/mail/root"
                    },
                    "PATH": {
                        "__ansible_unsafe": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
                    },
                    "PWD": {
                        "__ansible_unsafe": "/home/ubuntu"
                    },
                    "SHELL": {
                        "__ansible_unsafe": "/bin/bash"
                    },
                    "SUDO_COMMAND": {
                        "__ansible_unsafe": "/bin/sh -c echo BECOME-SUCCESS-cuuwsmpnkygrjxdzbuhcvukrtapxtdvl ; /usr/bin/python3 /home/ubuntu/.ansible/tmp/ansible-tmp-1696370640.9211326-55828-29546402818259/AnsiballZ_setup.py"
                    },
                    "SUDO_GID": {
                        "__ansible_unsafe": "1001"
                    },
                    "SUDO_UID": {
                        "__ansible_unsafe": "1000"
                    },
                    "SUDO_USER": {
                        "__ansible_unsafe": "ubuntu"
                    },
                    "TERM": {
                        "__ansible_unsafe": "xterm-256color"
                    },
                    "USER": {
                        "__ansible_unsafe": "root"
                    }
                },
                "ansible_eth0": {
                    "active": true,
                    "device": {
                        "__ansible_unsafe": "eth0"
                    },
                    "features": {
                        "esp_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "esp_tx_csum_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "fcoe_mtu": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "generic_receive_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "generic_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "highdma": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "hsr_dup_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_ins_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_rm_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hw_tc_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "l2_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "large_receive_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "loopback": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "macsec_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "netns_local": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "ntuple_filters": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "receive_hashing": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_all": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_checksumming": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "rx_fcs": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_hw": {
                            "__ansible_unsafe": "on"
                        },
                        "rx_gro_list": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_gro_forwarding": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_tunnel_port_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_filter": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "rx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_hw_parse": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tcp_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "tls_hw_record": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_rx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_tx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_fcoe_crc": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ip_generic": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_checksum_ipv4": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ipv6": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_sctp": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksumming": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_esp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_fcoe_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_list": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_partial": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_robust": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_ipxip4_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_ipxip6_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_lockless": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_nocache_copy": {
                            "__ansible_unsafe": "off"
                        },
                        "tx_scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_scatter_gather_fraglist": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_sctp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_tcp6_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_ecn_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_mangleid_segmentation": {
                            "__ansible_unsafe": "off"
                        },
                        "tx_tcp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tunnel_remcsum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_tnl_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_tnl_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_stag_hw_insert": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "vlan_challenged": {
                            "__ansible_unsafe": "off [fixed]"
                        }
                    },
                    "hw_timestamp_filters": [],
                    "ipv4": {
                        "address": {
                            "__ansible_unsafe": "X.X.X.X"
                        },
                        "broadcast": {
                            "__ansible_unsafe": ""
                        },
                        "netmask": {
                            "__ansible_unsafe": "X.X.X.X"
                        },
                        "network": {
                            "__ansible_unsafe": "X.X.X.X"
                        }
                    },
                    "ipv6": [
                        {
                            "address": {
                                "__ansible_unsafe": "fe80::XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                            },
                            "prefix": {
                                "__ansible_unsafe": "64"
                            },
                            "scope": {
                                "__ansible_unsafe": "link"
                            }
                        }
                    ],
                    "macaddress": {
                        "__ansible_unsafe": "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX"
                    },
                    "module": {
                        "__ansible_unsafe": "virtio_net"
                    },
                    "mtu": 1500,
                    "pciid": {
                        "__ansible_unsafe": "virtio0"
                    },
                    "promisc": false,
                    "speed": -1,
                    "timestamping": [],
                    "type": {
                        "__ansible_unsafe": "ether"
                    }
                },
                "ansible_fibre_channel_wwn": [],
                "ansible_fips": false,
                "ansible_form_factor": {
                    "__ansible_unsafe": "Other"
                },
                "ansible_fqdn": {
                    "__ansible_unsafe": "epdp5uqbf5e36dpsf45h.auto.internal"
                },
                "ansible_host": "X.X.X.X",
                "ansible_hostname": {
                    "__ansible_unsafe": "epdp5uqbf5e36dpsf45h"
                },
                "ansible_hostnqn": {
                    "__ansible_unsafe": ""
                },
                "ansible_interfaces": [
                    {
                        "__ansible_unsafe": "eth0"
                    },
                    {
                        "__ansible_unsafe": "lo"
                    }
                ],
                "ansible_is_chroot": false,
                "ansible_iscsi_iqn": {
                    "__ansible_unsafe": "iqn.2004-10.com.ubuntu:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX8a60af82"
                },
                "ansible_kernel": {
                    "__ansible_unsafe": "5.15.0-79-generic"
                },
                "ansible_kernel_version": {
                    "__ansible_unsafe": "#86-Ubuntu SMP Mon Jul 10 XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX UTC 2023"
                },
                "ansible_lo": {
                    "active": true,
                    "device": {
                        "__ansible_unsafe": "lo"
                    },
                    "features": {
                        "esp_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "esp_tx_csum_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "fcoe_mtu": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "generic_receive_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "generic_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "highdma": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "hsr_dup_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_ins_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hsr_tag_rm_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "hw_tc_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "l2_fwd_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "large_receive_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "loopback": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "macsec_hw_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "netns_local": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "ntuple_filters": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "receive_hashing": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_all": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_checksumming": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "rx_fcs": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_hw": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_gro_list": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_gro_forwarding": {
                            "__ansible_unsafe": "off"
                        },
                        "rx_udp_tunnel_port_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_filter": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "rx_vlan_stag_hw_parse": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "scatter_gather": {
                            "__ansible_unsafe": "on"
                        },
                        "tcp_segmentation_offload": {
                            "__ansible_unsafe": "on"
                        },
                        "tls_hw_record": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_rx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tls_hw_tx_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_fcoe_crc": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ip_generic": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_checksum_ipv4": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_ipv6": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_checksum_sctp": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_checksumming": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_esp_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_fcoe_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gre_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_list": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_gso_partial": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_gso_robust": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_ipxip4_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_ipxip6_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_lockless": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_nocache_copy": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_scatter_gather": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_scatter_gather_fraglist": {
                            "__ansible_unsafe": "on [fixed]"
                        },
                        "tx_sctp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp6_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_ecn_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_mangleid_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tcp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_tunnel_remcsum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_segmentation": {
                            "__ansible_unsafe": "on"
                        },
                        "tx_udp_tnl_csum_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_udp_tnl_segmentation": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_offload": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "tx_vlan_stag_hw_insert": {
                            "__ansible_unsafe": "off [fixed]"
                        },
                        "vlan_challenged": {
                            "__ansible_unsafe": "on [fixed]"
                        }
                    },
                    "hw_timestamp_filters": [],
                    "ipv4": {
                        "address": {
                            "__ansible_unsafe": "X.X.X.X"
                        },
                        "broadcast": {
                            "__ansible_unsafe": ""
                        },
                        "netmask": {
                            "__ansible_unsafe": "X.X.X.X"
                        },
                        "network": {
                            "__ansible_unsafe": "X.X.X.X"
                        }
                    },
                    "ipv6": [
                        {
                            "address": {
                                "__ansible_unsafe": "::1"
                            },
                            "prefix": {
                                "__ansible_unsafe": "128"
                            },
                            "scope": {
                                "__ansible_unsafe": "host"
                            }
                        }
                    ],
                    "mtu": 65536,
                    "promisc": false,
                    "timestamping": [],
                    "type": {
                        "__ansible_unsafe": "loopback"
                    }
                },
                "ansible_local": {},
                "ansible_lsb": {
                    "codename": {
                        "__ansible_unsafe": "jammy"
                    },
                    "description": {
                        "__ansible_unsafe": "Ubuntu 22.04.3 LTS"
                    },
                    "id": {
                        "__ansible_unsafe": "Ubuntu"
                    },
                    "major_release": {
                        "__ansible_unsafe": "22"
                    },
                    "release": {
                        "__ansible_unsafe": "22.04"
                    }
                },
                "ansible_lvm": {
                    "lvs": {},
                    "pvs": {},
                    "vgs": {}
                },
                "ansible_machine": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_machine_id": {
                    "__ansible_unsafe": "2300000765b92fb4b795c33373c790b1"
                },
                "ansible_memfree_mb": 999,
                "ansible_memory_mb": {
                    "nocache": {
                        "free": 1747,
                        "used": 216
                    },
                    "real": {
                        "free": 999,
                        "total": 1963,
                        "used": 964
                    },
                    "swap": {
                        "cached": 0,
                        "free": 0,
                        "total": 0,
                        "used": 0
                    }
                },
                "ansible_memtotal_mb": 1963,
                "ansible_mounts": [
                    {
                        "block_available": 940751,
                        "block_size": 4096,
                        "block_total": 2041586,
                        "block_used": 1100835,
                        "device": {
                            "__ansible_unsafe": "/dev/vda2"
                        },
                        "fstype": {
                            "__ansible_unsafe": "ext4"
                        },
                        "inode_available": 406471,
                        "inode_total": 524288,
                        "inode_used": 117817,
                        "mount": {
                            "__ansible_unsafe": "/"
                        },
                        "options": {
                            "__ansible_unsafe": "rw,relatime"
                        },
                        "size_available": 3853316096,
                        "size_total": 8362336256,
                        "uuid": {
                            "__ansible_unsafe": "ed465c6e-049a-41c6-8e0b-c8da348a3577"
                        }
                    },
                    {
                        "block_available": 0,
                        "block_size": 131072,
                        "block_total": 507,
                        "block_used": 507,
                        "device": {
                            "__ansible_unsafe": "/dev/loop0"
                        },
                        "fstype": {
                            "__ansible_unsafe": "squashfs"
                        },
                        "inode_available": 0,
                        "inode_total": 11906,
                        "inode_used": 11906,
                        "mount": {
                            "__ansible_unsafe": "/snap/core20/1822"
                        },
                        "options": {
                            "__ansible_unsafe": "ro,nodev,relatime,errors=continue"
                        },
                        "size_available": 0,
                        "size_total": 66453504,
                        "uuid": {
                            "__ansible_unsafe": "N/A"
                        }
                    },
                    {
                        "block_available": 0,
                        "block_size": 131072,
                        "block_total": 896,
                        "block_used": 896,
                        "device": {
                            "__ansible_unsafe": "/dev/loop1"
                        },
                        "fstype": {
                            "__ansible_unsafe": "squashfs"
                        },
                        "inode_available": 0,
                        "inode_total": 873,
                        "inode_used": 873,
                        "mount": {
                            "__ansible_unsafe": "/snap/lxd/24322"
                        },
                        "options": {
                            "__ansible_unsafe": "ro,nodev,relatime,errors=continue"
                        },
                        "size_available": 0,
                        "size_total": 117440512,
                        "uuid": {
                            "__ansible_unsafe": "N/A"
                        }
                    },
                    {
                        "block_available": 0,
                        "block_size": 131072,
                        "block_total": 399,
                        "block_used": 399,
                        "device": {
                            "__ansible_unsafe": "/dev/loop2"
                        },
                        "fstype": {
                            "__ansible_unsafe": "squashfs"
                        },
                        "inode_available": 0,
                        "inode_total": 496,
                        "inode_used": 496,
                        "mount": {
                            "__ansible_unsafe": "/snap/snapd/18357"
                        },
                        "options": {
                            "__ansible_unsafe": "ro,nodev,relatime,errors=continue"
                        },
                        "size_available": 0,
                        "size_total": 52297728,
                        "uuid": {
                            "__ansible_unsafe": "N/A"
                        }
                    },
                    {
                        "block_available": 0,
                        "block_size": 131072,
                        "block_total": 327,
                        "block_used": 327,
                        "device": {
                            "__ansible_unsafe": "/dev/loop3"
                        },
                        "fstype": {
                            "__ansible_unsafe": "squashfs"
                        },
                        "inode_available": 0,
                        "inode_total": 658,
                        "inode_used": 658,
                        "mount": {
                            "__ansible_unsafe": "/snap/snapd/20092"
                        },
                        "options": {
                            "__ansible_unsafe": "ro,nodev,relatime,errors=continue"
                        },
                        "size_available": 0,
                        "size_total": 42860544,
                        "uuid": {
                            "__ansible_unsafe": "N/A"
                        }
                    },
                    {
                        "block_available": 0,
                        "block_size": 131072,
                        "block_total": 508,
                        "block_used": 508,
                        "device": {
                            "__ansible_unsafe": "/dev/loop4"
                        },
                        "fstype": {
                            "__ansible_unsafe": "squashfs"
                        },
                        "inode_available": 0,
                        "inode_total": 11991,
                        "inode_used": 11991,
                        "mount": {
                            "__ansible_unsafe": "/snap/core20/2015"
                        },
                        "options": {
                            "__ansible_unsafe": "ro,nodev,relatime,errors=continue"
                        },
                        "size_available": 0,
                        "size_total": 66584576,
                        "uuid": {
                            "__ansible_unsafe": "N/A"
                        }
                    }
                ],
                "ansible_nodename": {
                    "__ansible_unsafe": "epdp5uqbf5e36dpsf45h"
                },
                "ansible_os_family": {
                    "__ansible_unsafe": "Debian"
                },
                "ansible_pkg_mgr": {
                    "__ansible_unsafe": "apt"
                },
                "ansible_proc_cmdline": {
                    "BOOT_IMAGE": {
                        "__ansible_unsafe": "/boot/vmlinuz-5.15.0-79-generic"
                    },
                    "biosdevname": {
                        "__ansible_unsafe": "0"
                    },
                    "console": {
                        "__ansible_unsafe": "ttyS0"
                    },
                    "net.ifnames": {
                        "__ansible_unsafe": "0"
                    },
                    "ro": true,
                    "root": {
                        "__ansible_unsafe": "UUID=ed465c6e-049a-41c6-8e0b-c8da348a3577"
                    }
                },
                "ansible_processor": [
                    {
                        "__ansible_unsafe": "0"
                    },
                    {
                        "__ansible_unsafe": "GenuineIntel"
                    },
                    {
                        "__ansible_unsafe": "Intel Core Processor (Haswell, no TSX)"
                    },
                    {
                        "__ansible_unsafe": "1"
                    },
                    {
                        "__ansible_unsafe": "GenuineIntel"
                    },
                    {
                        "__ansible_unsafe": "Intel Core Processor (Haswell, no TSX)"
                    }
                ],
                "ansible_processor_cores": 2,
                "ansible_processor_count": 1,
                "ansible_processor_nproc": 2,
                "ansible_processor_threads_per_core": 1,
                "ansible_processor_vcpus": 2,
                "ansible_product_name": {
                    "__ansible_unsafe": "xeon-e5-2660"
                },
                "ansible_product_serial": {
                    "__ansible_unsafe": "YC-epdp5uqbf5e36dpsf45h"
                },
                "ansible_product_uuid": {
                    "__ansible_unsafe": "23000007-65b9-2fb4-b795-c33373c790b1"
                },
                "ansible_product_version": {
                    "__ansible_unsafe": "pc-q35-yc-2.12"
                },
                "ansible_python": {
                    "executable": {
                        "__ansible_unsafe": "/usr/bin/python3"
                    },
                    "has_sslcontext": true,
                    "type": {
                        "__ansible_unsafe": "cpython"
                    },
                    "version": {
                        "major": 3,
                        "micro": 12,
                        "minor": 10,
                        "releaselevel": {
                            "__ansible_unsafe": "final"
                        },
                        "serial": 0
                    },
                    "version_info": [
                        3,
                        10,
                        12,
                        {
                            "__ansible_unsafe": "final"
                        },
                        0
                    ]
                },
                "ansible_python_version": {
                    "__ansible_unsafe": "3.10.12"
                },
                "ansible_real_group_id": 0,
                "ansible_real_user_id": 0,
                "ansible_selinux": {
                    "status": {
                        "__ansible_unsafe": "Missing selinux Python library"
                    }
                },
                "ansible_selinux_python_present": false,
                "ansible_service_mgr": {
                    "__ansible_unsafe": "systemd"
                },
                "ansible_ssh_host_key_dsa_public": {
                    "__ansible_unsafe": "AAAAB3NzaC1kc3MAAACBALJULpMF8H6LOicdBhCk/Vcej+LyZ/dJnO78PLokKIq3ve95DbQDbixWlTRdJedvZPMNTR7ygSvSIAAijTPfwvsBgqxARAKaZtu8f6jZCywPzJIVH5vE1cuW/EVgIZCljEmmuYERtZL8ur4XX6m1zvmvpdUYFsobbBrRg4w/DRB5AAAAFQDfjMg/B9utqS1nWkFMGMXPeR2D7wAAAIBqtQnrkVFJBqPIk7/qwZAdTraO8jSKXB/TxXeSmkcjpCNYWv1Ap3yUmO2AFYiAN91dw2o4gAntnr0uKg1dIzFvqcLwuXK8CxTkNpZTe77U5wNA4HyhQwqEEuBtclT3zlw376nxJZcHlgKO5CaweC5gCX1nIMcMEfrwACBL9fMvFAAAAIEAkg6nO0K25u5OmRvuhA38wwFPq3/8E9gtp4hVhaxcW/DeavC5DoT3ZSw9ktxGGScdb6cJH7F16iQePCXsHTu9FjSwaHdDyjkak4/t2HP5Pj7QxgdYLf117EG3V7Gxv0qn0+0DEdHq3JDRzAnYU2lq4kK1cYbgF4G2oLHm79z6wxg="
                },
                "ansible_ssh_host_key_dsa_public_keytype": {
                    "__ansible_unsafe": "ssh-dss"
                },
                "ansible_ssh_host_key_ecdsa_public": {
                    "__ansible_unsafe": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBKHdK19C9lD3WYCEJJcNI1/uhcPqFWvB5rB/YOlqJrESy9l1FbAPXz6kzHVMba4qmsHL1w0fRFik+bJTZktQqU="
                },
                "ansible_ssh_host_key_ecdsa_public_keytype": {
                    "__ansible_unsafe": "ecdsa-sha2-nistp256"
                },
                "ansible_ssh_host_key_ed25519_public": {
                    "__ansible_unsafe": "AAAAC3NzaC1lZDI1NTE5AAAAIMklw4anlYEf3iiyxnG8/J+6AZAO3VosIOtE1R6kntKP"
                },
                "ansible_ssh_host_key_ed25519_public_keytype": {
                    "__ansible_unsafe": "ssh-ed25519"
                },
                "ansible_ssh_host_key_rsa_public": {
                    "__ansible_unsafe": "AAAAB3NzaC1yc2EAAAADAQABAAABgQCWRQ5gkPZdWzAlWotzZufJyNqbauVvkxEMYqiMFjyas37Ovw19Whv6GLXCQYC/ZPZJ/xRCb5LrxwbHU/vxoo4+RS636bRDa5wwitom7SyJ/sgl84bypm7MSLUrroKsTzMFUiaPseGSljsfvI5j4ljh8jXPSn25v36RGlvtbHCWqV6YhjuGlaVASr0p+AJsrpIkK7RYknN0+8Jp0SJDsPI2X8wsv7gFndmy71iXgO3D/QgxuEjLgLe5i0PhIzW+cyskaCktSgsbd0Dc5YTCb3KCsN2HRTSLMBg4D+ASQNy7LNRPFDHqY1f/IRT+3SHrEy09zR68XG9kjNkjmX5ydVP+Uce/FR4gO82ycc4F5MghkLHog3ndy9RNRnMiZD0cMkj4eTRpxQRsUyHKI7Fgrd9Qgj2GyPdGB78Py5+2c0QEsMXjIVgDFnMOAeejo6szU+kjCtqk46P5FvhXtft8POFYiq7xn6/xeGepC8h1aXAfyIJ+L7aMOWY5+evkzZKg8bU="
                },
                "ansible_ssh_host_key_rsa_public_keytype": {
                    "__ansible_unsafe": "ssh-rsa"
                },
                "ansible_swapfree_mb": 0,
                "ansible_swaptotal_mb": 0,
                "ansible_system": {
                    "__ansible_unsafe": "Linux"
                },
                "ansible_system_capabilities": [],
                "ansible_system_capabilities_enforced": {
                    "__ansible_unsafe": "False"
                },
                "ansible_system_vendor": {
                    "__ansible_unsafe": "Yandex"
                },
                "ansible_uptime_seconds": 5979,
                "ansible_user_dir": {
                    "__ansible_unsafe": "/root"
                },
                "ansible_user_gecos": {
                    "__ansible_unsafe": "root"
                },
                "ansible_user_gid": 0,
                "ansible_user_id": {
                    "__ansible_unsafe": "root"
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 0,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "NA"
                },
                "boot_disk.#": "1",
                "boot_disk.0.auto_delete": "<error>",
                "boot_disk.0.device_name": "epdpdq9nilnnofbtb58s",
                "boot_disk.0.disk_id": "epdpdq9nilnnofbtb58s",
                "boot_disk.0.initialize_params": "<error>",
                "boot_disk.0.mode": "READ_WRITE",
                "created_at": "2023-10-03TXXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXXZ",
                "description": "",
                "discovered_interpreter_python": {
                    "__ansible_unsafe": "/usr/bin/python3"
                },
                "filesystem.#": "0",
                "folder_id": "b1g3jmubid9buevdcjn8",
                "fqdn": "epdp5uqbf5e36dpsf45h.auto.internal",
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "gpu_cluster_id": "",
                "hostname": "",
                "id": "epdp5uqbf5e36dpsf45h",
                "labels": "<error>",
                "local_disk.#": "0",
                "metadata.#": "1",
                "metadata.ssh-keys": "ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCrEh8AEeHWANb5uETRc31s0ffXAYKnqdqVxIgf0TmgM8xmegNf7IC8aOBqdYaqXTHU77ilksExY9VsQJSBvQiw+2+n9v7F1vneJErV+UWuYSwJBxAEVB8IcIvcGNAGADnKQ/P/H9rhAT46yP6+L4C43mYByIR1mnOfChtl00zKGTw23MLMPTK25W6gz0XkpK41Btl0/hIB1dlVLE/BOQ8tDh9aKHGbzrmqxw2hOQhgnoZnnfsk/pQM4aE3GONiVqsMY6gnQhDqIguPnlm49FDAG/RIR59XSwzarF/7pIywWlG6wQxAXscFZESqFNDPz+uCTrWe5vQTgFVKMKmI/WPRbTMHbwNDbV+iaAzLJaZbSnaeYteJ/augpDzMr1lNqAR7DwmTrBkua+5MwwLU88ekNl1j92K0vu0ykLSCNbWIZNEhC7kOUVYSYPlqOnTWpfkTJwPd5WPisEbd4biKbnpn3tPNjf04+1R3Qlj8shNlTCeA4Bpgn5zQ2MXmbUz3ytqM9aMqdtHvst65HSx8R8q3jYDss1ABXMEgwLILADZT3cCwM7gnxb5+qm0dZo/XBHiSJ2K9YSyWKLHktIBdDeDx4P254RXRial63Y+tLDlH5zJJx9F0xB/XGIucXSfZLL3GVs0ZWS6r2dPKaQFZVowy4mfktR4/znb6cnox2wHEmw== yacloud-admin\n\n",
                "metadata_options.#": "1",
                "metadata_options.0.aws_v1_http_endpoint": "<error>",
                "metadata_options.0.aws_v1_http_token": "<error>",
                "metadata_options.0.gce_http_endpoint": "<error>",
                "metadata_options.0.gce_http_token": "<error>",
                "module_setup": true,
                "name": "terraform-vm",
                "network_acceleration_type": "standard",
                "network_interface.#": "1",
                "network_interface.0.dns_record": "<error>",
                "network_interface.0.index": "<error>",
                "network_interface.0.ip_address": "X.X.X.X",
                "network_interface.0.ipv4": "<error>",
                "network_interface.0.ipv6": "<error>",
                "network_interface.0.ipv6_address": "",
                "network_interface.0.ipv6_dns_record": "<error>",
                "network_interface.0.mac_address": "XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX",
                "network_interface.0.nat": "<error>",
                "network_interface.0.nat_dns_record": "<error>",
                "network_interface.0.nat_ip_address": "X.X.X.X",
                "network_interface.0.nat_ip_version": "IPV4",
                "network_interface.0.security_group_ids": "<error>",
                "network_interface.0.subnet_id": "e2ljd90kbm6l958e3651",
                "placement_policy.#": "1",
                "placement_policy.0.host_affinity_rules": "<error>",
                "placement_policy.0.placement_group_id": "",
                "platform_id": "standard-v1",
                "resources.#": "1",
                "resources.0.core_fraction": "<error>",
                "resources.0.cores": "<error>",
                "resources.0.gpus": "<error>",
                "resources.0.memory": "<error>",
                "scheduling_policy.#": "1",
                "scheduling_policy.0.preemptible": "<error>",
                "secondary_disk.#": "0",
                "service_account_id": "",
                "status": "running",
                "timeouts": "<error>",
                "zone": "ru-central1-b"
            }
        }
    },
    "all": {
        "children": [
            "type_yandex_compute_instance",
            "ungrouped",
            "vm_1",
            "vm_1_0"
        ]
    },
    "type_yandex_compute_instance": {
        "hosts": [
            "X.X.X.X"
        ]
    },
    "vm_1": {
        "hosts": [
            "X.X.X.X"
        ]
    },
    "vm_1_0": {
        "hosts": [
            "X.X.X.X"
        ]
    }
}

```