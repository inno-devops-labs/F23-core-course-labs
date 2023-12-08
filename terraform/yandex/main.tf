terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone = "ru-central1-a"
}

resource "yandex_vpc_network" "network" {
  name = "tf-network"
}

resource "yandex_vpc_subnet" "subnetwork" {
  name           = "tf-network-ru-central1-a"
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["10.128.0.0/24"]
}

resource "yandex_compute_image" "ubuntu" {
  source_family = "ubuntu-2004-lts"
}

resource "yandex_compute_instance" "vm" {
  name = "devops"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = yandex_compute_image.ubuntu.id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnetwork.id
    nat = true
  }
}