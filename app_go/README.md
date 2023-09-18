# Web app on Golang

## Description 

The simple web application where show the weather on specific city. 
To choose city you should write name of the city on url, then the app will return temperature of this city.

## Getting start

### How to build

+ Make sure that Docker installed
+ To build docker run this command `docker build -t rkbekzat/weather .`

### How to pull 
+ Run this command `docker pull rkbekzat/weather`

### How To run 
+  Run this command `docker run -p 3000:3000 rkbekzat/weather`

+  Open the any browser and write this url `localhost:3000/"name_of_city"`

![](example.png)

### CI workflow
The CI workflow will be triggered when we push to github repository. There are 2 jobs, such as build and security.
The build job will check linter, test and security after installing dependencies. The docker job will automatically push change to a docker hub.