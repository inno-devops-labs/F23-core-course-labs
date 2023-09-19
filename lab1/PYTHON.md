# Python best practices

Azamat Shakirov B20-CS

a.shakirov@innopolis.university



## Framework

**Flask**

I used flask because of its simplicity, flexibility, and documentation. With flask, you can easily dynamically define text, build APIs, and handle user input, making it an excellent choice for scalable and maintainable web applications

##  Libraries

**Pytz**

 I used pytz due to its comprehensive database of time zone information and its ease of use. With pytz, you can accurately convert and manipulate dates and times across different time zones, ensuring consistent and correct time-related operations in your applications

**Flake8**

Flake8 is considered one of the best Python linters for code quality, style consistency, and the ability to catch potential errors, resulting in cleaner, more maintainable code

**Pytest**

Pytest is considered the best testing framework for Python because of its simplicity, powerful features, extensive plugin ecosystem, and efficient test discovery, making it a popular choice for writing and executing tests in Python projects



## Unit Tests

**Test fixtures** 

Test fixtures are used to set up the necessary environment for testing. In this example, two fixtures are defined: `app` and `client`. The `app` fixture is responsible for creating a copy of the Flask app using the `return_flask_app_copy` function from the `main` module. The `client` fixture uses the `app` fixture to create a test client for making HTTP requests to the app.

**Test function**

The `test_get_time` function is a test case that verifies the behavior of the `/` endpoint of the Flask app. It takes the `client` fixture as an argument, indicating that the fixture should be used to provide the test client.

**Assertion statements**

Assertion statements are used to verify the expected behavior of the code being tested. In this example, several assertion statements are used to check the response status code and the response data. For example, `assert response.status_code == 200` checks that the response status code is 200, indicating a successful request. Similarly, `assert response.data.decode() == get_moscow_time_without_timezone()` checks that the response data matches the expected Moscow time without using *Pytz* library.

**Test isolation**

Each test function is isolated from other test functions, meaning that they are independent and do not interfere with each other. This is achieved by using test fixtures to set up the necessary environment for each test.

**Test readability**

The code is written in a way that makes it easy to read and understand the purpose of each test case. The function and variable names are descriptive, and comments are provided to explain the purpose of certain code sections, such as the emulation of page refresh.