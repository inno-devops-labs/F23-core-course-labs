## Python app

### Prepare to work
Install packages, pre-commit via `make init` command (be sure, you have **make** on your machine)
- Run `source venv/bin/activate` to run venv (and `deactivate` to off the venv)
- Run `pip install -r requirements.txt` to install packages

Also use `make lint` and `make typechek` to increase code quality while dev process

### Run web app
`make run`

### Test running
Be sure that you have installed dev packages (`pip install -r requirements.txt`)
To test app enter `make test` in your terminal.


### DockerHub images
 1. python: https://hub.docker.com/r/dashvayet/lab2_app_python/tags
 2. cpp: https://hub.docker.com/r/dashvayet/cpp_app