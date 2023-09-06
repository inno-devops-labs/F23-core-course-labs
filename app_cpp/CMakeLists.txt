cmake_minimum_required(VERSION 3.1)
project(app_cpp)

set(CMAKE_CXX_STANDARD 17)
MESSAGE(STATUS "Using toolchain file: ${CMAKE_TOOLCHAIN_FILE}")

find_package(Boost REQUIRED COMPONENTS asio)
include_directories(${Boost_INCLUDE_DIRS})


add_executable(TestCMakeDemo main.cpp)
target_link_libraries(TestCMakeDemo PUBLIC Boost::system)

