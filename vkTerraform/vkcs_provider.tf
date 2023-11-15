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
    username = "evgn.worker@gmail.com"

    # The password of the account
    password = "YOUR_PASSWORD"

    # The tenant token can be taken from the project Settings tab - > API keys.
    # Project ID will be our token.
    project_id = "2cd713920a2443fa9c08c5e4f0208c82"
    
    # Region name
    region = "RegionOne"
    
    auth_url = "https://infra.mail.ru:35357/v3/" 
}
