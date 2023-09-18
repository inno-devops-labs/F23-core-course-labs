## Current Moscow time Web app 

A simple web app where show current time in moscow.

### Development 

Using `pytz` library we found timezone of moscow, and using `datatime` with `pytz` we find the current time 

### To testing 

+ Run this command in terminal `pytest`

## Getting start

### How to build

+ Make sure that Docker installed
+ To build docker run this command `docker build -t rkbekzat/mosconw_time .`

### How to pull
+ Run this command `docker pull rkbekzat/moscow_time`

### How To run
+  Run this command `docker run -p 8080:8080 rkbekzat/moscow_time`

### Unit Tests
+ The unit test is important part of developing because in the future when the project will be extend, the unit test will help prevent bugs and cover some corner cases.


### CI workflow 
The CI workflow will be triggered when we push to github repository. There are 3 jobs, such as build, docker and security. 
The build job will check linter and test after installing dependencies. The docker job will automatically push change to a docker hub. 
And last, job security is responsible for checking vulnerabilities in projects.