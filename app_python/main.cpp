#include <iostream>
#include <string>
#include <ctime>
#include <chrono>
#include <iomanip>
#include <sstream>

int main() {
    // Fetch current time
    std::time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());

    // Convert the current time to Moscow's timezone
    std::tm* localTime = std::localtime(&now);
    localTime->tm_hour += 3;  // Moscow is 3 hours ahead of GMT

    // Format the time as a string
    std::stringstream ss;
    ss << std::put_time(localTime, "%F %T");

    // Display the current time in Moscow
    std::cout << "Current time in Moscow: " << ss.str() << std::endl;
 
    return 0;
}