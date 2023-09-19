# Lab1 - Python Web Application Best Practices

In this lab, I have developed a Python web application that displays the current time in Moscow using the Flask framework.

## Framework Choice

I chose Flask for several reasons:

- **Simplicity**: Flask's minimalist design provides essential web development tools without unnecessary complexity, aligning with project's requirements.

- **Ease of Learning**: Flask's beginner-friendly nature allowed me to quickly launch the project with minimal knowledge in web development.

- **Testing Support**: Flask offers built-in testing support, ensuring the reliability and correctness of application.

## Coding Standards
I followed the Python Enhancement Proposal 8 (PEP 8) guidelines, adhering to consistent naming conventions, indentation, and code structure.

## Testing

To verify the functionality and correctness of web application, I implemented unit tests using Python's `unittest` framework. The `test_app.py` file contains test cases that assess the application's response and ensure that the displayed time updates upon page refreshing. 
## Code Quality

I emphasized code quality throughout the development process:

- Breaking code into modules, promoting reusability and maintainability.

- Ensuring that each component of application has a clear and distinct responsibility.

- Adding comments to code for clarity and documentation.
- ## Unit Tests

I have implemented unit tests for the Python web application to ensure its functionality and correctness. These tests adhere to best practices in Python testing:

- **Test Framework**: I used Python's built-in `unittest` framework for organizing and running unit tests.

- **Test Coverage**: I aimed to achieve comprehensive test coverage, including testing the main functionality of the application and edge cases.

- **Isolation**: Each test case is isolated to ensure that they do not rely on the state of other tests.

- **Descriptive Test Names**: I provided descriptive names for each test case and test method to make it clear what each test is checking.
