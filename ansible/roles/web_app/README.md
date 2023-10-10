## Ansible web_app role

My role can prepare the environment for app (install pip/docker/docker-compose), wipe old docker container by request and deploy docker app by pulling it from the dockerhub.

## Tags
The tasks are marked by different tags:
- tag `prepare` is placed on tasks that prepare the environment for the subsequent deploy step. It installs pip and docker/docker-compose if it still not on the instance.
- tag `wipe` is placed on cleaning jobs - this jobs stops the running container of the same app before running current launch.
- tag `deploy` is placed on jobs that responsible for pulling, running the container and cleaning the previous one. The wipe job is included because the new container cannot run at the same time with the old one.


## Variables
The role also has a couple of variables:
Boolean variable `web_app_full_wipe` needs to be set to `true` if user wants to enable the wipe job that stops previously running containers. Not required during the first launch.
The variable `application_port` must be set to the port on which application runs inside the docker container. This port will be mapped to port `80` so that the client could easily open the page in browser(with default port) and see how the application works.


## Role usage

Prepare environment, wipe old containers and deploy new container:
`ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml -e web_app_full_wipe=true`

Skip prepare phase:
`ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml -e web_app_full_wipe=true --skip-tags prepare`

Wipe only:
`ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml -e web_app_full_wipe=true --tags wipe`


## Results check

As a result the docker container will be started on the instance:
`ubuntu@ip-172-31-16-121:~$ sudo docker ps`
```
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS      NAMES
61872eea89d9   klemencja/app_python   "/bin/sh -c 'python3…"   9 seconds ago   Up 8 seconds   8000/tcp   web_app_python
```

As well as the application itself would work on port `80`:
![img.png](../../resources/running_application_on_aws_80.png)