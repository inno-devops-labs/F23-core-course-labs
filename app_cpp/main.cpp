#include <iostream>
#include <boost/asio.hpp>
#include <boost/asio/steady_timer.hpp>
#include <ctime>

using namespace boost::asio;
using ip::tcp;

std::string get_current_time() {
    std::time_t current_time = std::time(nullptr);
    std::tm* moscow_time = std::gmtime(&current_time);
    std::string buffer;
    buffer.resize(80);
    std::strftime(buffer.data(), buffer.size(), "%Y-%m-%d %H:%M:%S", moscow_time);
    return buffer;
}

void start_server() {
    while(true) {
        io_context io;

        tcp::acceptor acceptor(io, tcp::endpoint(tcp::v4(), 8080));
        tcp::socket socket(io);

        acceptor.accept(socket);

        // Generate HTTP response with Moscow time
        std::string response = "HTTP/1.1 200 OK\r\n"
                               "Content-Type: text/html\r\n\r\n"
                               "<h2>Current Moscow Time: " + get_current_time() + "</h2>";

        // Write the response back to the client
        boost::asio::write(socket, boost::asio::buffer(response));

        // Close the connection
        socket.shutdown(tcp::socket::shutdown_send);
    }
}

int main() {
    try {
        start_server();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}