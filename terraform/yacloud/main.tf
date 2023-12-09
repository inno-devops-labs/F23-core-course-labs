# Terraform configuration for provisioning a virtual machine in Yandex Cloud

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = var.az
}

# Provision a virtual machine
resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name

  resources {
    cores  = var.vm_cores
    memory = var.vm_ram
  }

  boot_disk {
    initialize_params {
      image_id = var.os_image_id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = var.ssh_pubkey 
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = var.az 
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}