#include "Server.hpp"
#include <boost/asio.hpp>
#include <fstream>
#include <iostream>

int guessingNumber = 234;

bool is_number(const std::string &s) {
    return !s.empty() && std::find_if(s.begin(),
                                      s.end(), [](unsigned char c) { return !std::isdigit(c); }) == s.end();
}

[[noreturn]] void start_server(int port, int cycle) {
    boost::asio::io_context io_service;
    boost::asio::ip::tcp::acceptor acceptor(io_service,
                                            boost::asio::ip::tcp::endpoint(boost::asio::ip::tcp::v4(), port));

    for(int i = 0; i < cycle || cycle == -1;) {
        if (cycle != -1) {
            ++i;
        }
        boost::asio::ip::tcp::socket socket(io_service);
        acceptor.accept(socket);

boost::asio::ip::tcp::endpoint endpoint = socket.remote_endpoint();
std::cout << "Connected to: " << endpoint.address() << ':' << endpoint.port() << '\n';

        boost::asio::streambuf buffer;
        boost::asio::read_until(socket, buffer, "\r\n\r\n");

        std::string method, path, http_version;
        std::istream request_stream(&buffer);
        request_stream >> method >> path >> http_version;
std::cout << method << '\n' << path << "\n\n";

        std::string response = "HTTP/1.1 200 OK\r\n"
                               "Content-Type: text/html\r\n\r\n";


        std::string htmlResponse;
        std::ifstream in("index.html");
        std::string str((std::istreambuf_iterator<char>(in)),
                        std::istreambuf_iterator<char>());
        response += str;

        std::string newMessage;
        std::string messageStr = "message=";
        size_t messageIt = path.find(messageStr);
        if (messageIt != std::string::npos) {
            auto strNumber = path.substr(messageIt + messageStr.size(), std::string::npos);
            if (is_number(strNumber)) {
                int num = std::stoi(strNumber);
                if (num == guessingNumber) {
                    newMessage = "You win!";
                } else if (num < guessingNumber) {
                    newMessage = "You write smaller number then guessing number";
                } else {
                    newMessage = "You write bigger number then guessing number";
                }

                std::string paste = "<h1>Number 1 to 1000</h1>";
                size_t toPaste = response.find(paste);
                response.insert(toPaste + paste.size(), "<h2>" + newMessage + "</h2>");
            }
        }

        boost::asio::write(socket, boost::asio::buffer(response));
    }
}