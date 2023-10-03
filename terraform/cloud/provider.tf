terraform {
    required_providers {
        vkcs = {
            source = "vk-cs/vkcs"
            version = "~> 0.1.12" 
        }
    }
}

provider "vkcs" {
    # Your user account.
    username = "g.nguyen@innopolis.university"

    # The password of the account
    password = var.vk_cloud_access_key

    # The tenant token can be taken from the project Settings tab - > API keys.
    # Project ID will be our token.
    project_id = "d249e628601146e8b4238ea23ea64956"
    
    # Region name
    region = "RegionOne"
    
    auth_url = "https://infra.mail.ru:35357/v3/" 
}
