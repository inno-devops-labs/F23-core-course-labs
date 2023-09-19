# PYTHON.md

## Justification for Using Flask

Flask is one of the most popular frameworks for writing web applications in python.

- **Simplicity**: While it would be a con for a big project, for this application flask allows to write it much easier.
- **Ease of learning**: Python isn't my main language, so it was one of the most trivial libraries to pick up.
- **Extensibility**: Flask is very extensible, and allows to add new features easily, and as this is the skeleton for next labs, it's probably important.

## Implementation of Best Practices and Coding Standards

- **PEP8**: I've used PEP8 to check my code for style errors.
- **Comments**: I've added comments to my code to make it easier to understand? but not overcomplicated it.
- **Gitignore**: I've added a gitignore file to ignore the virtual environment and the cache. Used [this site](https://www.toptal.com/developers/gitignore) for generating proper gitignore.
- **Readme**: I've added a readme file to explain how to run the application and what it does.
- **Structure**: I've tried to make the structure of the project as clear as possible, and to separate the logic from the templates.
- **Tests**: I've added tests to make sure the application works as expected

## Use of linters

I've used pylint to check my code for errors and style issues and markdownlint extensions to check my markdown files for errors.

## Testing

I've used `unittest` to test my application. It tests the following:

- The application returns the correct time.
- We can access the application.

I've also developed these tests using the best practices for testing:

- **Coverage**: Tests cover all functions of the application - they test both time and availability of the page.
- **Assertive Testing**: Tests use assertions to ensure that the responses from the API are as expected. This includes checking the status code and the content of the page.
- **Test Separation**: Keeping tests separate from application code. Store them in a dedicated directory, such as "tests."
- **Arrange-Act-Assert pattern**: Each test uses AAA pattern: Arrange (set up the test environment), Act (perform the action being tested), and Assert (verify the expected outcome).
