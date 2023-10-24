# Ansible Role: Showing Time Application
Installs and runs via docker image:

```
app_name: app_python
docker_image_name: IlyaMirzazhanov/app_python
docker_image_version: 1.0.0
docker_container_name: app_python_container
internal_port: 8080
external_port: 8080

docker_image: "{{ docker_image_name }}:{{ docker_image_version }}"
app_dir: "/{{ app_name }}"
docker_compose_filepath: "{{ app_dir }}/docker-compose.yml"

web_app_full_stop: true

web_app_full_wipe: true

web_app_deployment_way: "docker"
```

# Deploy
* Using Docker
* Using Docker-compose