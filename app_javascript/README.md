## Lab 1

I decided to use javascript because I have little experience using it. An interesting fact is that Javascript is the most popular programming language in the world and is in great demand among various organizations.

## Description
Web server which shows page with current time

## Run server 
```
node main.js
```

## Docker
### How to build?
```
docker build -t seakysneka1/webserv_js .
```
### How to pull?
```
docker pull seakysneka1/webserv_js:latest
```
### How to run?
```
docker run -p 5000:5000 seakysneka1/webserv_js
```