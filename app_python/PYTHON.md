## Table of Contents

1. [Goal](#1-Goal)

2. [Steps](#2-Steps)

3. [Best Practices](#3-Best-Practices)


# Goal

- Write a python web-server production ready app
- Test the web-server

# Steps

- Create [app_python](../app_python) directory and initialize a virtual environment with `python -m venv venv`
- Install required project dependencies with `pip install` then freeze the environment with `pip freeze > requirements.txt`
- Implement application logic.
- Create a [PYTHON.md](../app_python/PYTHON.md) with description and instructions for local development.
- Add `pytest` to project dependencies and freeze the environment.
- Create [tests](https://github.com/Sh3b0/DevOps/app_python/tests) module with a `test_<unit>.py` file for each test unit.
- Run `python -m pytest` to verify tests are working

# Best practices

- Use **Flask debugging server**, this will:
  - Log all requests in terminal and reload server on code changes.
  - Allow accessing debug info from the app when errors occur.
- Work in a **virtual environment**
  - Write dependencies with their versions in `requirements.txt` for the `venv` to be reproducible by other programmers who will work on the project.
  - Using a `venv` also isolates the project and avoids polluting your OS file system with unnecessary packages that will take space and make indexing slower and may result in dependency conflicts.
- **Follow PEP8 style guide** and enforce it with tools and extensions
  - For example: configure `autopep8` to run on save in the IDE.
- **Follow recommended directory structure and directory/file naming. Example:**
  - Use `templates` directory for HTML templates and `static` directory for static files with subdirectories for `css`, `js`, `images`, and any other needed static files.
- To connect Python webapps to the webserver, we need a **Web Server Gateway Interface (WSGI)** 
- Use an appropriate testing framework (e.g., `pytest`).
- Use a recommended directory hierarchy for organizing tests.
- Add an `__init__` script to the directory (even if empty) to mark it as a module and to avoid unintended code execution when importing the test module.

