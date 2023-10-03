terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  token     = var.yandex_cloud_token
  cloud_id  = var.yandex_cloud_id
  folder_id = var.yandex_cloud_folder_id
  zone      = "ru-central1-a"
}

data "yandex_compute_image" "last_ubuntu" {
  family = "ubuntu-2204-lts"
}

data "yandex_vpc_subnet" "default_a" {
  name = "default-ru-central1-a"
}

resource "yandex_compute_instance" "default" {
  name        = var.yandex_cloud_vm_name
  platform_id = "standard-v1"

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.last_ubuntu.id
    }
  }

  network_interface {
    subnet_id = data.yandex_vpc_subnet.default_a.subnet_id
    nat       = true
  }

  resources {
    core_fraction = 5
    cores         = 2
    memory        = 1
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519-cloud.pub")}"
  }
}