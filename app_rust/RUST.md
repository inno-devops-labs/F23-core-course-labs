## Table of Contents

1. [Goal](#1-Goal)

2. [Steps](#2-Steps)

3. [Best Practices](#3-Best-Practices)

4. [How to run](#4-How-To-Run)

5. [Docker](#5-Docker)



# Goal

- Write a rust web-server app
- Test the running web server

# Steps

- Create [app_rust](../app_rust) directory and initialize a cargo project with `cargo new web_server`
- Install required project dependencies with `cargo.toml`
- Implement application logic.
- Create a [RUST.md](../app_rust/Rust.md) with description and instructions for local development.
- Go to the local Ip to test the project.

# Best practices

- Use lib file to handle the logic:
  - main will only build and run the code from lib.
- Delegate Errors handling in lib to be caught within the main
  - make build and run functions return a **Result enum** with required result or the Error caught
- **Use rust analyzer** and enforce it with tools and extensions.
  - enoforces rust rules
  - autoformtes

- **Follow recommended directory structure and directory/file naming. Example:**
  - Use `templates` directory for HTML templates and `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files.
- write a test module in lib for any of unit tests
- make sure the webserver handles concurrent requests



# How to run

## Requirements

- Install Rust

  ```shell
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  ```

## How to run

1. build the project using cargo

   ```shell
   cargo build --release
   ```

2. Run the executable

   ```she 
   ./target/release/web_server
   ```

3. Go to `127.0.0.1:5000`

# Docker

## Requirements

Make sure you have docker on your machine

- ```she
  sudo apt install docker.io
  ```

## Steps

- To build and run a docker image yourself run:

```shell
Docker build -t <your_tag> .
docker run -it -p 5000:5000 <your_tag>
```

- To use the image on docker hub

  ```shell
  Docker login
  docker pull el3os/moscow_time_rust
  docker run -p 5000:5000 el3os/moscow_time_rust 
  ```

  
