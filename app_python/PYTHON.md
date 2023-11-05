# Python, Flask framework

---------------------------------------------------

## Table of Contents

- [Choice Justification](#choice-justification)
- [Applied Best Practices](#applied-best-practices)
  - [Project Structure](#1-project-structure)
  - [Pre-commit Hooks](#2-pre-commit-hooks)
  - [Virtual Environment](#3-virtual-environment)
  - [.gitignore](#4-gitignore)
  - [Testing with Pytest](#5-testing-with-pytest)
  - [README.md](#6-readmemd)

---------------------------------------------------

## Choice Justification

- Flask is good choice for simple apps, which is our case.
- Easy to use and learn.
- Easy to test.

---------------------------------------------------

## Applied Best Practices

This document outlines the best practices followed in our project to ensure code quality, maintainability.

### 1. Project Structure

We have organized our project into a clear and consistent structure. This structure enhances code readability and maintainability. 

### 2. Pre-commit Hooks

We've integrated pre-commit hooks into our development workflow. These hooks automate code quality checks and formatting before any commits are made. Specifically, we use the following tools:

- **Flake8**: A linter to enforce Python code style and check for code quality issues.
- **Black**: An auto-formatter that helps maintain consistent code formatting throughout the project.

### 3. Virtual Environment

To isolate our project's dependencies and ensure consistency across different environments, we use virtual environments. This practice allows us to manage dependencies and versions effectively, reducing potential conflicts with other projects.

### 4. .gitignore

We have a well-defined `.gitignore` file in place to exclude unnecessary files and directories from version control. This ensures that sensitive information and build artifacts are not committed to the repository.

### 5. Testing with Pytest

Testing is a crucial aspect of our development process. We use [Pytest](https://pytest.org/) as our testing framework. This allows us to write comprehensive unit tests, integration tests, and end-to-end tests to verify the functionality and reliability of our code.

> ### Unit tests
> 1. Unit test to check the content of the webpage
> 2. Unit test to check, if time updates on refresh
> ### Best practices applied
> - Written appropriate test names
> - Created simple unit tests
> - Each unit tests addressed a single use-case
> - Test coverage is higher than 90%
> - Unit tests designed to be fast


### 6. Requirements

We maintain a `requirements.txt` file to list all the project's dependencies and their respective versions. This practice offers several benefits:

- **Dependency Management**: It simplifies the process of managing and installing project dependencies, making it easier to set up a development environment.
- **Version Consistency**: By specifying exact versions of dependencies, we ensure that all team members are using the same versions, reducing potential compatibility issues.
- **Reproducibility**: It enables us to recreate the exact environment, facilitating debugging and testing.


### 7. README.md

We maintain a detailed `README.md` file to provide essential information about our project. Our README includes the following:

- Project description and purpose.
- Installation and setup instructions.
- Usage examples and guidelines.

By following these best practices, we ensure that our project remains organized, code quality is upheld.
