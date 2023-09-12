#include "../src/Server.hpp"
#include <iostream>
#include <thread>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

void test1() {
    std::thread t1(start_server, 8080, 1);

    boost::asio::io_service io_service;
    tcp::resolver resolver(io_service);
    tcp::resolver::query query("127.0.0.1", "8080");
    tcp::resolver::iterator endpoint_iterator = resolver.resolve(query);

    tcp::socket socket(io_service);
    boost::asio::connect(socket, endpoint_iterator);

    boost::asio::streambuf request;
    std::ostream request_stream(&request);
    request_stream << "GET / HTTP/1.1\r\n";
    request_stream << "Host: 127.0.0.1\r\n";
    request_stream << "Accept: */*\r\n";
    request_stream << "Connection: close\r\n\r\n";

    boost::asio::write(socket, request);

    boost::asio::streambuf response;
    boost::asio::read_until(socket, response, "\r\n");

    // Check that response is OK.
    std::istream response_stream(&response);
    std::string http_version;
    response_stream >> http_version;
    unsigned int status_code;
    response_stream >> status_code;
    std::string status_message;
    std::getline(response_stream, status_message);
    if (!response_stream || http_version.substr(0, 5) != "HTTP/")
    {
        std::cout << "Invalid response\n";
        return;
    }
    if (status_code != 200)
    {
        std::cout << "Response returned with status code " << status_code << "\n";
        return;
    }

    boost::asio::read_until(socket, response, "\r\n\r\n");

    boost::system::error_code error;
    if (error != boost::asio::error::eof)
    {
        std::cout << "Error: " << error;
    }

    std::cout << "\nTest pass\n";
    t1.join();
}

int main() {
   test1();
}