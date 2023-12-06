### Best practices:
* Do not hardcode secrets - for dockerhub and snyk use repo secrets
* Do not hardcode variables - for docker image name, tag and etc. use variables
* Cache gradle step
* Cache docker image building
* All actions are minimal
* Use SNYK vulnerability checker
* Limit scope of workflow for SNYK
* Set timeouts for workflows