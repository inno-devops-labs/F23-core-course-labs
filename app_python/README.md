## Current Moscow time Web app 

A simple web app where show current time in moscow.

### Development 

Using `pytz` library we found timezone of moscow, and using `datatime` with `pytz` we find the current time 


## Getting start

### How to build

+ Make sure that Docker installed
+ To build docker run this command `docker build -t rkbekzat/mosconw_time .`

### How to pull
+ Run this command `docker pull rkbekzat/moscow_time`

### How To run
+  Run this command `docker run -p 8080:8080 rkbekzat/moscow_time`
