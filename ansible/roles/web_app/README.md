# Ansible Web_app role 
## Description 
This ansible role deploys web app using docker compose and creates new `data` volume.

## Requirements:
* Docker role
  * Configure variables in defaults.main.yml:
      ```
      # Tasks variables
      web_app_full_wipe: false
      app_dir: "/{{ app_name }}"
    
      # Docker compose variables
      docker_compose_path: "{{ app_dir }}/docker-compose"
      docker_compose_file: 'docker-compose.yml'
      docker_compose_file_path: "{{ docker_compose_path }}/{{ docker_compose_file }}"
    ```
    * Configure variables in playbook:
      ```
        vars:
          docker_container: 'app_python'
          docker_image_name: 'lnsfna/app_python'
          docker_image_version: 'latest'
          internal_port: 8080
          external_port: 8080
          app_name: 'app_python'
      ```

## Usage:

Include `web_app` role in your playbook 
```
- name: Deploy Python app in Docker
  hosts: all
  become: yes
  roles:
    - name: web_app
```