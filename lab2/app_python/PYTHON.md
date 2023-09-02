To develop an app, I've decided to use aiohttp framework:
+ since the task doesn't require much, it's better to stick with minimalistic solutions rather than bloated
+ for web applications, async code is generally a good practice instead of hard-to-develop and hard-to-debug multithreaded code and poor-performing synchronous code
+ it is a good opportunity to me to explore new framework

I've decided to take a test-driven approach so I've written tests before implementing certain functionality in the application. I have chosen Pytest as a testing framework.

Coding standards are ensured by code linters. I have used flake8 linter for this tasks and autopep8 to auto-fix linting issues.