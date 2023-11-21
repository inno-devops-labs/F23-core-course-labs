## Python app

### Prepare to work
Install packages, pre-commit via `make init` command (be sure, you have **make** on your machine)
- Run `source venv/bin/activate` to run venv (and `deactivate` to off the venv)
- Run `pip install -r requirements.txt` to install packages

Also use `make lint` and `make typechek` to increase code quality while dev process

### Run web app
`make run`

### Unit tests
Be sure that you have installed dev packages (`pip install -r requirements.txt`)
To test app enter `make test` in your terminal.

### Access the application 
 - ```http://<addressOfDeployedApp>:<portOfDeployedApp>/``` - access the time handler
 - ```http://<addressOfDeployedApp>:<portOfDeployedApp>/visits``` - access the visits counter


You can also use curl or any other http requester for access with respective parameters and endpoint
### DockerHub images
 1. python: https://hub.docker.com/r/dashvayet/lab2_app_python/tags
 2. cpp: https://hub.docker.com/r/dashvayet/cpp_app

### CI workflow
#### Testing code and dependencies
1. CI starting with creating environment essential for running necessary checks, all installed deps are cached for optimization of workflow
2. Then we apply Snyk scanning for installed dependencies to ensure all deps are safe to use
3. When CI ensures that used environment is safe it starting to  use Linters for checking source code quality
4. After steps described above CI ready to run unit test for checking functional quality of provided source code
#### Building and deploying
1. Workflow continues with logining in dockerhub to be able to push new image in public space afterwards. Login is created using actions credentials as docker user name and access token which is highly secure
2. After previously declared steps workflow starting to build and push docker image, it deploys built docker image on github using name from creds
3. Build is cahced for optimization of fututre build
#### Checking Docker image with snyk
1. After workflow completes building and publishing it is checking for vulnerabilities using Snyk