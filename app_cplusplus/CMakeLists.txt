cmake_minimum_required(VERSION 3.1)
project(app_cpp)

set(CMAKE_CXX_STANDARD 17)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

find_package(Boost REQUIRED COMPONENTS asio)
include_directories(${Boost_INCLUDE_DIRS})

configure_file(templates/index.html ${CMAKE_CURRENT_BINARY_DIR}/index.html COPYONLY)

add_executable(Ruslan src/main.cpp ${CMakeDemo_TEST_SRC} ${CMakeDemo_TEST_HEADER})
target_link_libraries(Ruslan PUBLIC Boost::system)
