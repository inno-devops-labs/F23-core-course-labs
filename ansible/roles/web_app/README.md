
## Web App Role 

This role are responsible for pulling docker image "rkBekzat/weather" from docker hub and running.

## Requirements 

VM

## Dependencies 

Docker role which located on `ansible/role/docker`

## Usage

`Playbook:`


```
 - name: Deploy python app
  hosts: all
  become: true
  roles:
    - name: web_app
      tags: python_web_app
      vars:
        app_name: "app_python"
        docker_container: "moscow_time"
        docker_image: "rkBekzat/moscow_time"
        docker_image_tag: "latest"
        internal_port: 5000
        external_port: 8000
 ```