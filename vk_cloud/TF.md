Result of ```terraform show```:

```
# data.vkcs_compute_flavor.compute:
data "vkcs_compute_flavor" "compute" {
    disk         = 20
    extra_specs  = {
        "agg_common"     = "true"
        "hw:cpu_sockets" = "1"
        "mcs:cpu_type"   = "standard"
    }
    flavor_id    = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    is_public    = true
    name         = "Basic-1-2-20"
    ram          = 2048
    rx_tx_factor = 1
    swap         = 0
    vcpus        = 1
}

# data.vkcs_images_image.compute:
data "vkcs_images_image" "compute" {
    checksum         = "6d4ade04c95ed136e8c0f2832ee31cd2"
    container_format = "bare"
    created_at       = "2022-08-15T14:12:15Z"
    disk_format      = "raw"
    file             = "/v2/images/b75595ca-4e1d-47e0-8e95-7a02edc0e242/file"
    id               = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
    metadata         = {}
    min_disk_gb      = 0
    min_ram_mb       = 0
    most_recent      = false
    name             = "Ubuntu-22.04-202208"
    owner            = "9d013ed7c41e4bf38dd91f899e40185a"
    protected        = false
    region           = "RegionOne"
    schema           = "/v2/schemas/image"
    size_bytes       = 3758096384
    tags             = []
    updated_at       = "2022-08-16T06:01:24Z"
    visibility       = "public"
}

# data.vkcs_networking_network.extnet:
data "vkcs_networking_network" "extnet" {
    admin_state_up       = "true"
    all_tags             = [
        "dm.semenov",
        "rivalsec123qwerty",
    ]
    external             = true
    id                   = "298117ae-3fa4-4109-9e08-8be5602be5a2"
    name                 = "ext-net"
    private_dns_domain   = "openstacklocal."
    region               = "RegionOne"
    sdn                  = "neutron"
    shared               = "true"
    subnets              = [
        "01009166-1de2-413d-995c-8c2272f1bc19",
        "0dbaf324-1c17-4c51-ab6f-817a2223a097",
        "13b6afaa-a0da-4ffb-8061-f7b28d318fdf",
        "191efdda-cd5a-4327-987d-1eb1b5b32b4d",
        "1e68063b-96e0-45bc-b010-579e9aabb485",
        "1ea7f321-4ed0-4ae7-a136-a0226b9c5969",
        "2267f99b-83a5-49b6-ba19-e0cbac642583",
        "389a5241-76e3-48b9-89f5-5b0a938cf8b3",
        "41d17c6b-d2cf-4bd2-8784-f8a846656c3b",
        "489f81ad-2a0c-449d-8aed-1876ddbd7840",
        "5a66e4b1-1676-444e-94cf-eb37ac80d464",
        "62a77e13-ccc0-44b7-8cac-0567163a8a3b",
        "7f876978-01fe-43ab-8c77-7e6e32cd28c4",
        "888682e5-abdd-4274-853f-b091115cce84",
        "94640c6b-6298-40d0-8c71-6aab8716d48f",
        "aa2689f9-a208-4bf2-bed0-c20dab001467",
        "b1911f6b-9185-45fd-a0c2-424b0c9155ce",
        "b2298251-6be3-444b-b213-59c66e25346b",
        "b5502dbd-18c7-4f44-857a-5819265bbbdc",
        "be8539d5-eeff-4eaa-8048-9f7c3dbc8804",
        "be9cabcf-c5f8-4e88-9e27-c5ba80f4a638",
        "c4f89da6-529f-4a08-9df1-6b95842a07b9",
        "c6fafdba-deb7-4ad0-83fd-ec893dedfb69",
        "cbd9c937-5339-42df-b0a7-edfb2ccfee59",
        "d10ef821-cba1-476c-bcfd-582632939e80",
        "d5f70b09-6d49-445b-99f1-184d366decf6",
        "ec5d4a62-5039-460c-833f-7084a19794d2",
    ]
    tenant_id            = "c9fe9505fdde4de680679748c7cfee7e"
    vkcs_services_access = false
}

# vkcs_compute_floatingip_associate.fip:
resource "vkcs_compute_floatingip_associate" "fip" {
    floating_ip = "212.233.95.103"
    id          = "212.233.95.103/34de1adc-e02d-4c82-98e6-97a422eb6d67/"
    instance_id = "34de1adc-e02d-4c82-98e6-97a422eb6d67"
    region      = "RegionOne"
}

# vkcs_compute_instance.compute:
resource "vkcs_compute_instance" "compute" {
    access_ip_v4        = "192.168.199.20"
    all_metadata        = {}
    all_tags            = []
    availability_zone   = "MS1"
    flavor_id           = "25ae869c-be29-4840-8e12-99e046d2dbd4"
    flavor_name         = "Basic-1-2-20"
    force_delete        = false
    id                  = "34de1adc-e02d-4c82-98e6-97a422eb6d67"
    image_id            = "Attempt to boot from volume - no image supplied"
    key_pair            = "keypair-terraform"
    name                = "compute-instance"
    power_state         = "active"
    region              = "RegionOne"
    security_groups     = [
        "default",
        "security_group",
    ]
    stop_before_destroy = false

    block_device {
        boot_index            = 0
        delete_on_termination = true
        destination_type      = "volume"
        source_type           = "image"
        uuid                  = "b75595ca-4e1d-47e0-8e95-7a02edc0e242"
        volume_size           = 8
        volume_type           = "ceph-ssd"
    }

    network {
        access_network = false
        fixed_ip_v4    = "192.168.199.20"
        mac            = "fa:16:3e:a2:52:3e"
        name           = "net"
        uuid           = "5ca4dc8f-1273-4e01-afa4-a5013854df5e"
    }
}

# vkcs_networking_floatingip.fip:
resource "vkcs_networking_floatingip" "fip" {
    address = "212.233.95.103"
    id      = "792bfa40-637a-413b-af29-51137af68a65"
    pool    = "ext-net"
    region  = "RegionOne"
    sdn     = "neutron"
}

# vkcs_networking_network.network:
resource "vkcs_networking_network" "network" {
    admin_state_up        = true
    all_tags              = []
    id                    = "5ca4dc8f-1273-4e01-afa4-a5013854df5e"
    name                  = "net"
    port_security_enabled = true
    private_dns_domain    = "mcs.local."
    region                = "RegionOne"
    sdn                   = "neutron"
    tags                  = []
    vkcs_services_access  = false
}

# vkcs_networking_port.port:
resource "vkcs_networking_port" "port" {
    admin_state_up         = true
    all_fixed_ips          = [
        "192.168.199.23",
    ]
    all_security_group_ids = [
        "0232b39e-6149-43cd-a4c4-27ac19d4ffec",
        "e4e4f65b-79c6-4d61-a0fb-478893b24258",
    ]
    all_tags               = []
    dns_assignment         = [
        {
            "hostname"   = "host-192-168-199-23"
            "ip_address" = "192.168.199.23"
        },
    ]
    id                     = "8dec7801-5ac7-40d0-8729-939109432bbe"
    mac_address            = "fa:16:3e:0c:cf:00"
    name                   = "port_1"
    network_id             = "5ca4dc8f-1273-4e01-afa4-a5013854df5e"
    port_security_enabled  = true
    region                 = "RegionOne"
    sdn                    = "neutron"
    tags                   = []

    fixed_ip {
        ip_address = "192.168.199.23"
        subnet_id  = "4155ada3-88c4-41bd-a229-2a9ce84d0a68"
    }
}

# vkcs_networking_port_secgroup_associate.port:
resource "vkcs_networking_port_secgroup_associate" "port" {
    all_security_group_ids = [
        "0232b39e-6149-43cd-a4c4-27ac19d4ffec",
        "e4e4f65b-79c6-4d61-a0fb-478893b24258",
    ]
    enforce                = false
    id                     = "8dec7801-5ac7-40d0-8729-939109432bbe"
    port_id                = "8dec7801-5ac7-40d0-8729-939109432bbe"
    region                 = "RegionOne"
    sdn                    = "neutron"
    security_group_ids     = [
        "0232b39e-6149-43cd-a4c4-27ac19d4ffec",
    ]
}

# vkcs_networking_router.router:
resource "vkcs_networking_router" "router" {
    admin_state_up      = true
    all_tags            = []
    external_network_id = "298117ae-3fa4-4109-9e08-8be5602be5a2"
    id                  = "c5f62b48-bbc2-4fde-a71b-b24e76f04d0c"
    name                = "router"
    region              = "RegionOne"
    sdn                 = "neutron"
    tags                = []
}

# vkcs_networking_router_interface.db:
resource "vkcs_networking_router_interface" "db" {
    id        = "eede4079-a502-411f-ab6a-dd3cdda8c0fe"
    port_id   = "eede4079-a502-411f-ab6a-dd3cdda8c0fe"
    region    = "RegionOne"
    router_id = "c5f62b48-bbc2-4fde-a71b-b24e76f04d0c"
    sdn       = "neutron"
    subnet_id = "4155ada3-88c4-41bd-a229-2a9ce84d0a68"
}

# vkcs_networking_secgroup.secgroup:
resource "vkcs_networking_secgroup" "secgroup" {
    all_tags    = []
    description = "terraform security group"
    id          = "0232b39e-6149-43cd-a4c4-27ac19d4ffec"
    name        = "security_group"
    region      = "RegionOne"
    sdn         = "neutron"
    tags        = []
}

# vkcs_networking_secgroup_rule.secgroup_rule_1:
resource "vkcs_networking_secgroup_rule" "secgroup_rule_1" {
    description       = "secgroup_rule_1"
    direction         = "ingress"
    ethertype         = "IPv4"
    id                = "b2956d83-5d56-4ceb-a408-1a404dbb87d6"
    port_range_max    = 22
    port_range_min    = 22
    protocol          = "tcp"
    region            = "RegionOne"
    remote_ip_prefix  = "0.0.0.0/0"
    sdn               = "neutron"
    security_group_id = "0232b39e-6149-43cd-a4c4-27ac19d4ffec"
}

# vkcs_networking_secgroup_rule.secgroup_rule_2:
resource "vkcs_networking_secgroup_rule" "secgroup_rule_2" {
    direction         = "ingress"
    ethertype         = "IPv4"
    id                = "cbbab4e5-8d5b-495c-ab38-62dc852bcf6f"
    port_range_max    = 3389
    port_range_min    = 3389
    protocol          = "tcp"
    region            = "RegionOne"
    remote_ip_prefix  = "0.0.0.0/0"
    sdn               = "neutron"
    security_group_id = "0232b39e-6149-43cd-a4c4-27ac19d4ffec"
}

# vkcs_networking_subnet.subnetwork:
resource "vkcs_networking_subnet" "subnetwork" {
    all_tags        = []
    cidr            = "192.168.199.0/24"
    dns_nameservers = []
    enable_dhcp     = true
    gateway_ip      = "192.168.199.1"
    id              = "4155ada3-88c4-41bd-a229-2a9ce84d0a68"
    name            = "subnet_1"
    network_id      = "5ca4dc8f-1273-4e01-afa4-a5013854df5e"
    no_gateway      = false
    region          = "RegionOne"
    sdn             = "neutron"
    tags            = []

    allocation_pool {
        end   = "192.168.199.254"
        start = "192.168.199.2"
    }
}


Outputs:

instance_fip = "212.233.95.103"

```


Result of ```terraform state list```
```
data.vkcs_compute_flavor.compute
data.vkcs_images_image.compute
data.vkcs_networking_network.extnet
vkcs_compute_floatingip_associate.fip
vkcs_compute_instance.compute
vkcs_networking_floatingip.fip
vkcs_networking_network.network
vkcs_networking_port.port
vkcs_networking_port_secgroup_associate.port
vkcs_networking_router.router
vkcs_networking_router_interface.db
vkcs_networking_secgroup.secgroup
vkcs_networking_secgroup_rule.secgroup_rule_1
vkcs_networking_secgroup_rule.secgroup_rule_2
vkcs_networking_subnet.subnetwork
```


Result of ```terraform output```
```
instance_fip = "212.233.95.103"
```