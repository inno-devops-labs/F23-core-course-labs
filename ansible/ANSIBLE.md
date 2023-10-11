# Ansible
I decided to follow some points from https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#directory-layout and decided to put playbooks into the root of project

## Docker role
Last 50 lines of the output from deployment command:
```
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [[---]]

TASK [docker : Ensure unnecessary, unofficial or old packages are removed] *****
ok: [[---]]

TASK [docker : Install docker] *************************************************
The following packages were automatically installed and are no longer required:
  apport-symptoms bc bolt fwupd fwupd-signed gir1.2-packagekitglib-1.0
  libappstream4 libarchive13 libatasmart4 libblockdev-fs2 libblockdev-loop2
  libblockdev-part-err2 libblockdev-part2 libblockdev-swap2 libblockdev-utils2
  libblockdev2 libdw1 libflashrom1 libftdi1-2 libfwupd2 libfwupdplugin5
  libgcab-1.0-0 libglib2.0-bin libgpgme11 libgstreamer1.0-0 libgudev-1.0-0
  libgusb2 libintl-perl libintl-xs-perl libjcat1 libjson-glib-1.0-0
  libjson-glib-1.0-common libmbim-glib4 libmbim-proxy libmm-glib0
  libmodule-find-perl libmodule-scandeps-perl libmspack0 libnspr4 libnss3
  libpackagekit-glib2-18 libparted-fs-resize0 libproc-processtable-perl
  libqmi-glib5 libqmi-proxy libsmbios-c2 libsort-naturally-perl libstemmer0d
  libtcl8.6 libterm-readkey-perl libudisks2-0 libxmlb2 libxmlsec1
  libxmlsec1-openssl libxslt1.1 lxd-agent-loader modemmanager needrestart
  open-vm-tools packagekit packagekit-tools python3-automat python3-bcrypt
  python3-blinker python3-chardet python3-click python3-colorama
  python3-configobj python3-constantly python3-debconf python3-debian
  python3-distro-info python3-distupgrade python3-hamcrest python3-hyperlink
  python3-incremental python3-jeepney python3-jwt python3-keyring
  python3-lazr.uri python3-oauthlib python3-problem-report python3-pyasn1
  python3-pyasn1-modules python3-pyparsing python3-secretstorage
  python3-service-identity python3-systemd python3-twisted
  python3-update-manager python3-wadllib python3-zope.interface sbsigntool
  secureboot-db squashfs-tools tcl tcl8.6 udisks2 unattended-upgrades
  usb-modeswitch usb-modeswitch-data zerofree
Use 'sudo apt autoremove' to remove them.
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  docker-ce-rootless-extras libltdl7 pigz docker-compose-plugin
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
0 upgraded, 4 newly installed, 0 to remove and 198 not upgraded.
changed: [[---]]

TASK [docker : Install docker-compose] *****************************************
changed: [[---]]

PLAY RECAP *********************************************************************
[---]             : ok=7    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

Inventory:
The result was quite strange, most likely due to the fact that I used VK Сloud
```
❯ ansible-inventory -i inventory/ --list
{
    "_meta": {
        "hostvars": {
            "[---]": {
                "ansible_host": "[---]",
                "ansible_user": "ubuntu",
                "fixed_ip": "",
                "floating_ip": "[---]",
                "id": "[---]/cf002654-e770-47b7-ba59-0c7f33737392/",
                "instance_fip": "[---]",
                "instance_id": "cf002654-e770-47b7-ba59-0c7f33737392",
                "region": "RegionOne",
                "timeouts": "<error>",
                "wait_until_associated": "<error>"
            },
            "[---]": {
                "access_ip_v4": "[---]",
                "admin_pass": "<error>",
                "all_metadata.#": "0",
                "all_tags.#": "0",
                "ansible_host": "[---]",
                "availability_zone": "MS1",
                "block_device.#": "1",
                "block_device.0.boot_index": "<error>",
                "block_device.0.delete_on_termination": "<error>",
                "block_device.0.destination_type": "volume",
                "block_device.0.device_type": "",
                "block_device.0.disk_bus": "",
                "block_device.0.guest_format": "",
                "block_device.0.source_type": "image",
                "block_device.0.uuid": "2624c3c5-ad2e-4dc2-88b1-67357fb4c263",
                "block_device.0.volume_size": "<error>",
                "block_device.0.volume_type": "ceph-ssd",
                "config_drive": "<error>",
                "flavor_id": "16ac89ad-a1d8-415a-b387-4b9f46af546a",
                "flavor_name": "Basic-1-2-20",
                "force_delete": "<error>",
                "id": "cf002654-e770-47b7-ba59-0c7f33737392",
                "image_id": "Attempt to boot from volume - no image supplied",
                "image_name": "<error>",
                "instance_fip": "[EXTERNAL ---]",
                "key_pair": "albert_pc",
                "metadata": "<error>",
                "name": "compute-instance",
                "network.#": "1",
                "network.0.access_network": "<error>",
                "network.0.fixed_ip_v4": "[---]",
                "network.0.mac": "fa:16:3e:61:cb:50",
                "network.0.name": "net",
                "network.0.port": "",
                "network.0.uuid": "c29be26b-edfe-43b6-8e22-94023084cf5d",
                "network_mode": "<error>",
                "personality.#": "0",
                "power_state": "active",
                "region": "RegionOne",
                "scheduler_hints.#": "0",
                "security_groups.#": "2",
                "security_groups.0": "default",
                "security_groups.1": "security_group",
                "stop_before_destroy": "<error>",
                "tags.#": "0",
                "timeouts": "<error>",
                "user_data": "<error>",
                "vendor_options.#": "0"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vk_cloud",
            "compute",
            "compute_0",
            "fip",
            "fip_0",
            "type_vkcs_compute_instance"
        ]
    },
    "compute": {
        "hosts": [
            "[---]"
        ]
    },
    "compute_0": {
        "hosts": [
            "[---]"
        ]
    },
    "fip": {
        "hosts": [
            "[---]"
        ]
    },
    "fip_0": {
        "hosts": [
            "[---]"
        ]
    },
    "type_vkcs_compute_floatingip_associate": {
        "hosts": [
            "[---]"
        ]
    },
    "type_vkcs_compute_instance": {
        "hosts": [
            "[---]"
        ]
    },
    "vk_cloud": {
        "children": [
            "type_vkcs_compute_floatingip_associate"
        ]
    }
}
```

## Best practices
https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html

I was following the best practices from the official documentation and because of that I decided to store playbooks in the root of project