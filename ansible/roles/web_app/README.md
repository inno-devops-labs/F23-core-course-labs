# Docker Role

This role deploy specific web app

## Requirements:

- Docker role on

## How to use:

Here is example

```
- name: Name of job
  hosts: all
  become: true
  roles:
    - role: web_app
      image: test:latest
      ports:
        - 1000:100
        ...
        - 1:1
```
