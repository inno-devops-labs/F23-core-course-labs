# Python Web Application Development - Daniil Okrug

## Framework choosing:

- The Web application uses the Flask framework.
- Flask is a lightweight and easy-to-use framework that is well-suited for small to medium-sized web applications like this one.
- Flask has built-in support for testing through Flask-Testing and integrates well with popular testing libraries like pytest. This makes it easy to write and run tests, ensuring the reliability of application
- While Flask is a lightweight framework, it is also scalable. If your project evolves and requires additional features or complexity, Flask can handle it.
- Flask's simplicity often translates into better performance, especially for small applications. It doesn't introduce unnecessary overhead, making it suitable for applications where performance is a consideration.
- Flask can be deployed on various hosting platforms and cloud providers, giving you the flexibility to choose the deployment method that best suits your project's requirements.

### Best practices:

- I'm using Python Enhancement Proposal 8 (PEP 8) style guide for code formatting to ensure consistency and readability
- Project following Flask's recommended application structure, separating routes, templates, and static files
- Implemeted tests with pytest to cover different aspects of application. Coverage: 91%

## Tests

Four tests were created for the application using the pytest library.

1. Checking the index path for its existence and successful operation.
2. Checking the /time path for its operation and correctness of the returned data format.
3. Checking the time update on the application page
4. Check template index.html for correct content.

### Best Practices

- Test Separation: Keeping tests separate from application code. Store them in a dedicated directory, such as "tests."
- Test Function Names: Use descriptive function names for test cases that indicate what I'm testing (e.g., test_index_route, test_get_time_route).
- Arrange-Act-Assert (AAA): Structure each test using the AAA pattern: Arrange (set up the test environment), Act (perform the action being tested), and Assert (verify the expected outcome).
- Fixtures: Using pytest fixtures for common setup and teardown tasks. For example, I can create a fixture for creating a test client and configuring the app in a testing mode.
