## About role

There is created a `web_app` role. 
The purpose of the role is to set up a docker and docker-compose on VM, while also deploying the Python Web Application.

## Requirements

The role has a dependency on `docker` role. It is used to set up docker properly.

## Usage

The role can set up any docker image, stored in `defaults/main.yml` with name `python_web_app_image`.
To set up the path where to deploy the project on VM, make use of `python_web_app_path`.