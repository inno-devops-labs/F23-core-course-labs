terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}

data "yandex_compute_image" "container-optimized-image" {
  family = "container-optimized-image"
}

resource "yandex_compute_instance" "app-python-vm" {
  name = "app-python-vm"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.container-optimized-image.id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-app-python.id
    nat       = true
  }

  metadata = {
    user-data                    = file("user-data.yaml")
    docker-container-declaration = file("docker.yaml")
    serial-port-enable           = 1
  }
}

resource "yandex_vpc_network" "network-app-python" {
  name = "python-app-network"
}

resource "yandex_vpc_subnet" "subnet-app-python" {
  name           = "python-app-subnet"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-app-python.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}
