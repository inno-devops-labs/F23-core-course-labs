terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-b"
}

resource "yandex_compute_instance" "devops-vm" {
  name      = "devops-vm"
  folder_id = var.default_folder
  allow_stopping_for_update = true

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = "fd864gbboths76r8gm5f"
      size = 20
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.devops-subnet.id
    nat       = true
  }

  metadata = {
    user-data          = "${file("user-meta.yml")}"
    serial-port-enable = 1
  }
}

resource "yandex_vpc_network" "devops-network" {
  name      = "devops-network"
  folder_id = var.default_folder
}

resource "yandex_vpc_subnet" "devops-subnet" {
  name           = "devops-subnet"
  zone           = "ru-central1-b"
  network_id     = yandex_vpc_network.devops-network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  folder_id      = var.default_folder
}

output "internal_ip_address_devops-vm" {
  value = yandex_compute_instance.devops-vm.network_interface.0.ip_address
}

output "external_ip_address_devops-vm" {
  value = yandex_compute_instance.devops-vm.network_interface.0.nat_ip_address
}


variable "default_folder" {
  description = "this is the default folder on my cloud"
  default     = "b1ghg9pqn4eit8epv3e0"
}