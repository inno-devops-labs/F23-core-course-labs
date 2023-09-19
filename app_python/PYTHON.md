## Framework
I've chosen FastApi framework for my web application. FastApi supports asynchronous endpoints by default, this makes it better than others. Moreover, it's really fast and it has built in data type validation. 

## Best practices
1. Files are separated by their types (server endpoints, page templates and config are separated). Such structure is easier to expand and easier to navigate. 
2. Using env file. It's a common web server security practise  

## Coding standards and testing 
1. I'm following PEP8 coding standards: optimized imports, blank lines, naming conventions, etc. It's ensured by flake8 linter.
   Run `flake8 .` from `app_python` directory to check.
2. I've written unit tests to test endpoints responses. I use pytest for testing.
   Run `python3 -m pytest` from `tests` directory to check.

## Unit tests
I've implemented 3 unit tests for root, time and non-existent handlers, these tests cover all functionality (fetching time, generating html page).
Best practices that i've followed:
* Using FastApi test client to test responses.
* Test edge cases, using positive and negative tests
* Tests are independent and do not rely on each other