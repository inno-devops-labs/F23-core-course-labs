## Web App

### Variables

`defaults/main.yml` contain list of variables:

* `app_docker_image` Docker image name.

* `app_container_name` Docker container name.

* `app_port` Port.

* `app_wipe` Boolean to wipe.

### Tags

Use `pull` tag, to only perform the pull of the image.

Use `deploy` tag to perform/wipe deployment of the image.

Use `docker_compose` tag to add/wipe docker-compose.yml.