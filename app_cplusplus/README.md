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