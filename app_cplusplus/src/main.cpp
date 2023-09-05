#include <iostream>
#include <boost/asio.hpp>
#include <fstream>

int guessingNumber = 234;

bool is_number(const std::string &s) {
    return !s.empty() && std::find_if(s.begin(),
                                      s.end(), [](unsigned char c) { return !std::isdigit(c); }) == s.end();
}

[[noreturn]] void start_server(int port) {
    boost::asio::io_service io_service;
    boost::asio::ip::tcp::acceptor acceptor(io_service,
                                            boost::asio::ip::tcp::endpoint(boost::asio::ip::tcp::v4(), port));

    while (true) {
        boost::asio::ip::tcp::socket socket(io_service);
        acceptor.accept(socket);

        boost::asio::streambuf buffer;
        boost::asio::read_until(socket, buffer, "\r\n\r\n");

        std::string method, path, http_version;
        std::istream request_stream(&buffer);
        request_stream >> method >> path >> http_version;

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

int main(int argc, char *argv[]) {
    if (argc != 2 || !is_number(argv[1])) {
        std::cout << "Incorrect port\n";
        return 0;
    }
    int port = std::stoi(argv[1]);
    start_server(port);
}