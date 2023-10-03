## VKCloud

```shell
    terraform state list
```

* Output:
```text
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

```shell
   terraform state show data.vkcs_compute_flavor.compute
```

* Output:
```text
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

```


## Same for Docker