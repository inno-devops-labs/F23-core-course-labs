terraform {
    required_providers {
        vkcs = {
            source = "vk-cs/vkcs"
            version = "~> 0.1.12" 
        }
    }
}

provider "vkcs" {
    username = "esaian.mark@yandex.ru"
    password = var.cloud_pass
    project_id = "c13b1bb2fb9945229c8f29062ebb1310"
    region = "RegionOne"
    auth_url = "https://infra.mail.ru:35357/v3/" 
}
