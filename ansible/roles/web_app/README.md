## Web App Role

Use this role for deploying web app using docker compose

### Dependencies

Role uses `docker` role as dependency for installing pip, docker-compose and so on.

### Requirements

Before usage setup next variables:
```
docker_container:
docker_image_name:
docker_image_version:
docker_image: "{{ docker_image_name }}:{{ docker_image_version }}" # DO NOT CHANGE

docker_compose_path:
docker_compose_file:
docker_compose_file_path: "{{ docker_compose_path }}/{{ docker_compose_file }}" # DO NOT CHANGE

internal_port:
external_port:

web_app_full_wipe: <true/false>
web_app_dir:
```

### Usage 

Add role `web_app` to playbook and run `ansible-playbook <path to playbook>`