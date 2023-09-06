# Project meta-description

## Framework rationale
To develop an app, I've decided to use `aiohttp` framework:
+ since the task doesn't require much, it's better to stick with minimalistic solutions rather than bloated
+ for web applications, async code is generally a good practice instead of hard-to-develop and hard-to-debug multithreaded code and poor-performing synchronous code
+ it is a good opportunity to me to explore new framework

## Testing and Quality Assurance
I've decided to take a test-driven approach so I've written tests before implementing certain functionality in the application.
I have chosen Pytest as a testing framework. Granularity of tests varies from unit tests, testing distinct functions, to system tests, testing the whole app.

## Following coding standards
Coding standards are ensured by a code linter. I have chosen `flake8` linter for this task and `autopep8` to auto-fix linting issues.