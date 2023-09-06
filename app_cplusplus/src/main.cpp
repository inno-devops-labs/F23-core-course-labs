#include <iostream>
#include "Server.hpp"


int main(int argc, char *argv[]) {
    if (argc != 2 || !is_number(argv[1])) {
        std::cout << "Incorrect port\n";
        return 0;
    }
    int port = std::stoi(argv[1]);
    start_server(port);
}