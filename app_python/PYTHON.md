# PYTHON.md

## Justification for Using Flask

I chose Flask for this project due to its simplicity, ease of use, and suitability for small web applications. Reasons include:

- **Simplicity**: Flask offers a minimalistic approach, ideal for small projects.
- **Ease of Use**: It provides a straightforward way to create web apps in Python.
- **Suitability**: Flask's lightweight nature fits well for this project's scale.

## Implementation of Best Practices and Coding Standards

I adhered to best practices:

- **PEP 8**: Followed PEP 8 style guide for clean and consistent code.
- **Structure**: Maintained a clear separation of concerns.
- **Documentation**: Included comments and instructions for clarity.
- **Testing**: Web application is tested by simple Unit test case.
- **.gitignore**: No need to explain why we need this :>

# Testing the Application

To test the application you should run:

> `python -m unittest test_app`

Simple unit test to check if response from server is corresponds to actual time in moscow.

## Best practices

- Using assertesions for testing
- Test checks main funcionality of service - show moscow time at response moment
- Using testclient, so no need in hosting real service for testing
- Test is module, so it can be easily restructured
