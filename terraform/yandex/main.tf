terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"

    backend "s3" {
    endpoint = "storage.yandexcloud.net"
    bucket   = "chiplinka-default-backet"
    region   = "ru-central1"
    key      = "terraform-main.tfstate"

    skip_region_validation      = true
    skip_credentials_validation = true
  }
}

provider "yandex" {
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone = "ru-central1-a"
}
resource "yandex_compute_image" "ubuntu_2004" {
  source_family = "ubuntu-2004-lts"
}

resource "yandex_compute_instance" "vm_1" {
  name = "terraform-vm-1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = yandex_compute_image.ubuntu_2004.id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_1.id
    nat       = true
  }

  metadata = {
    ssh-keys           = "ubuntu:${file("~/.ssh/ublunta_2.pub")}"
    user-data          = "${file("~/Projects/core-course-labs/terraform/yandex/meta.txt")}"
    serial-port-enable = 1
  }
}

resource "yandex_vpc_network" "network_1" {
  name = "chiplinka-vpc-network-default"
}

resource "yandex_vpc_subnet" "subnet_1" {
  name           = "chiplinka-subnet-default-ru-central1-a"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network_1.id
  v4_cidr_blocks = ["10.130.0.0/24"]
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm_1.network_interface.0.ip_address
}