## Why I choosed Gjango:

1. Robustness: Django provides a lot of built-in features and tools that help developers to build complex web applications quickly and efficiently.

2. Scalability: Django is highly scalable and can handle a large number of users and requests without compromising performance.

3. Security: Django has many built-in security features, such as protection against SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).

## Best practices

1. Use version control: Version control systems like Git help developers to track changes made to their codebase and collaborate with other team members effectively. It also provides a backup of the codebase and allows developers to revert to the previous version if needed.

2. Write automated tests: Automated tests help to catch bugs early in the development process and ensure that the codebase is working as expected. Developers should write unit tests, integration tests, and end-to-end tests for their web application. I've implemented only unit tests for now.

3. Use a linter: A linter is a tool that analyzes code for potential errors and stylistic inconsistencies. It helps to ensure that the codebase follows coding standards and best practices.

## Unit Tests

This test verifies that the /current_time/ page returns the current time in Moscow. To run this test, you need to run the command:

`python manage.py test myapp.tests.CurrentTimeTestCase`

