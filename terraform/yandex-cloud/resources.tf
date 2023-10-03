data "yandex_compute_image" "my_image" {
  family = "ubuntu-1804-lts"
}

resource "yandex_compute_instance" "terraform" {
  name        = "devops-course-vm"
  platform_id = "standard-v1"

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.my_image.image_id
    }
  }

  network_interface {
    subnet_id      = yandex_vpc_subnet.terraform.id
    nat            = true
    nat_ip_address = yandex_vpc_address.addr.external_ipv4_address[0].address
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

resource "yandex_vpc_address" "addr" {
  name                = "public Ip"
  deletion_protection = false
  external_ipv4_address {
    zone_id = var.yandex_zone
  }
}

resource "yandex_vpc_network" "default" {
}

resource "yandex_vpc_subnet" "terraform" {
  network_id     = yandex_vpc_network.default.id
  v4_cidr_blocks = ["10.0.0.0/22"]
}
