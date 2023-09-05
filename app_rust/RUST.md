## Table of Contents

1. [Goal](#1-Goal)

2. [Steps](#2-Steps)

3. [Best Practices](#3-Best-Practices)


# Goal

- Write a rust web-server app
- Test the running web server

# Steps

- Create [app_rust](../app_rust) directory and initialize a cargo project with `cargo new web_server`
- Install required project dependencies with `cargo.toml`
- Implement application logic.
- Create a [RUST.md](../app_rust/Rust.md) with description and instructions for local development.
- Go to the local ip to test the project.

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
