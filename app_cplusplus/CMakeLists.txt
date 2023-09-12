cmake_minimum_required(VERSION 3.1)
project(app_cpp)

set(CMAKE_CXX_STANDARD 17)

find_package(Boost REQUIRED COMPONENTS system)
include_directories(${Boost_INCLUDE_DIRS})

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/templates/index.html ${CMAKE_CURRENT_BINARY_DIR}/index.html COPYONLY)

add_executable(startServer src/main.cpp ${CMakeDemo_TEST_SRC} ${CMakeDemo_TEST_HEADER} src/Server.cpp src/Server.hpp)
target_link_libraries(startServer PUBLIC ${Boost_LIBRARIES})

add_executable(checkServer test/checkServer.cpp src/Server.cpp src/Server.hpp)
target_link_libraries(checkServer PUBLIC ${Boost_LIBRARIES})