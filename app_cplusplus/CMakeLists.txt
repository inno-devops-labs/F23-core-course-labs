cmake_minimum_required(VERSION 3.1)
project(app_cpp)

set(CMAKE_CXX_STANDARD 17)

find_package(Boost REQUIRED COMPONENTS system)
include_directories(${Boost_INCLUDE_DIRS})

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/templates/index.html ${CMAKE_CURRENT_BINARY_DIR}/index.html COPYONLY)

add_library(Server src/Server.cpp)

add_executable(startServer src/main.cpp)
target_link_libraries(startServer PUBLIC ${Boost_LIBRARIES} Server)

if (TESTING)
    enable_testing()
    add_subdirectory(googletest)
    add_subdirectory(test)
endif ()