# Description

This web app is playing in guessing game! It takes numbers you say and gives you one of 3 answers
- You need less
- You need more
- You win

--------
# Build and run
    1. conan install . --output-folder=cmake-build-debug --build=missing
    2. cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -G Ninja -S app_cplusplus -B buildDirectory
    3. cmake --build ./buildDirectory
    4. Run 'startServer <port you want to run on>' from buildDirectory
    5. Run 'checkServer' target to test application


# Unit tests
To run unit testing you can run

    ./build/server_unit_tests 


# Access the application 
 - ```http://<addressOfDeployedApp>:<portOfDeployedApp>/``` - access the guessing game page
 - ```http://<addressOfDeployedApp>:<portOfDeployedApp>/visits``` - access the visits counter

You can also use curl or any other http requester for access with respective parameters and endpoint

### DockerHub images
 1. python: https://hub.docker.com/r/dashvayet/lab2_app_python/tags
 2. cpp: https://hub.docker.com/r/dashvayet/cpp_app

# Docker
For this app we need to establish environment and compile boost library, then we need to compile application and copy binary file to a next stage image where we can start application

1. To build  - run inside app_cplusplus
        
        docker build .
2.  To pull
    
        docker pull dashvayet/cpp_app
3.  To run

        docker run -ti -p <host port>:10000 dashvayet/cpp_app