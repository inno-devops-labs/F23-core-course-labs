#pragma once
#include <string>

bool is_number(const std::string &s);
[[noreturn]] void start_server(int port, int cycle = -1);