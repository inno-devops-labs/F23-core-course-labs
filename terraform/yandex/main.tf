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

resource "yandex_compute_instance" "vm-app-python" {
  name = "app-python-vm"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd808e721rc1vt7jkd0o"
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-app-python.id
    nat       = true
  }

  metadata = {
    user-data = "${file("user-data.yaml")}"
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
