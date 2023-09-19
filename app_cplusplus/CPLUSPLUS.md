# Arhitecture
At the first stage I don't think it is good idea to make a lot arhitect planning,
because in comparison to Python C++ force you to make much more and most probably you will change it in future iterations,
so I made a simple MVP that  is not optimize  yet, but it will be much more interesting to make it automized with deveops tricky things than Python

# Code practices
Smart const-ness guarantees, strict type mutations, all this used practices make c++ code clean, 
optimized and understandable 

# Framework choice
Boost is not a framework actually, it is a set of libraries that are pretending to be included into STL library
I have used as it is most powerful tool in C++ so if boost is included you can do everything.
which most probably will make docker image easier to create

# Unit testing
Tests checking that server operational and returns status code 200 for incoming responses
Tests are simple and easy to extend
Tests cover essential part - serverside working good, functional testing can be done, but not necessary on current stage of project

# CI WorkFlow
## Testing
1. CI starting with building boost, there is ubuntu + perl required which are tracked by snyk and have minor problems, but they are okay (nothing really dangerous)
2. Boost build is cached as it is really long process
3. Then workflow starting build cpp code
4. After steps above CI continues with unit testing
## Building Docker
1. CI logging in DockerHub
2. CI starting to build docker image and release image it on DockerHub
## Checking image
1. Snyk scanner cheeking used deps for vulnerabilities


    



