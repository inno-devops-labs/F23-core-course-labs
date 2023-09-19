### Justification of the flask framework:
- Flask was chosen because of its simplicity and minimalism, which makes it suitable for small-scale web applications like this one. Additionally, Flask follows Pythonic principles and coding standards, which align with best practices in Python development.

### Best practices:
0. **Virtual enviroment**
    
    I created a virtual environment for this project with commands:
    ```
        python -m venv venv
        source venv/bin/activate 
    ```
    And also exported variables:
    ```
        export FLASK_APP=application.app
        export FLASK_ENV=development
        flask run
    ```
1. **Project Structure:**
    - As a best practice I used a common structure of folders in flask project. A common structure includes folders for templates, static files, configuration, and application code.
2. **Blueprints**
    - I use flask blueprints to modularize my application. Blueprints help in breaking down my app into smaller, manageable components.
3. **Configuration Management**
    - I use configuration files (config.py) to store configuration variables, such as database URLs, secret keys, and environment-specific settings.
4. **Application of the Factory Pattern**
    - I create a Flask application using an application factory pattern. This makes my app more testable and allows me to configure different instances for development, testing, and production.
5. **Templates and Rendering**
    - Flask already has installed Jinja2 to render HTML. Sanitize user inputs to prevent XSS (Cross-Site Scripting) attacks.
6. **Testing** 
    - I implemented testing using pytest to test the routes.
        ```
        flask test
        ```
7. **Git ignore**

8. **Linters and tools**

    I ensured code quality with the following tools:

    - Black
        
        Black is an open-source code formatting tool for Python. Its primary purpose is to automatically format Python code according to the PEP 8 style guide and to enforce code formatting consistency across projects. 
    - Flake8

        Flake8 is a popular Python linting tool that helps developers maintain code quality and adhere to coding standards by analyzing Python code for potential issues and style violations. It is a widely used tool in the Python community and is often integrated into development workflows to ensure clean and consistent Python code.
        
9. **Pre-commit**
    -   A best practice for implementing pre-commit in a software project involves selecting relevant hooks such as code linters and formatters, centralizing configurations in a .pre-commit-config.yaml file and others.
        ```
        pre-commit install
        pre-commit run --all-files
        ```

### Code testing best practices:

In my python application in /tests/test_routes.py I created tests for checking if I can get moscow time and if moscow time changes on page refresh.

1. **Test Early and Continuously**
    - I created tests in the first lab and appended them in this lab. I also run tests always before in the pre-commit.
2. **Use Descriptive Test Names**
    - I write clear and descriptive test names that convey the purpose and expected behavior of the test.
3. **Keep Tests Independent**
    - In my application each test is independent and does not rely on the state or outcome of other tests. Tests should not have hidden dependencies.
4. **Use Test Fixtures:**
    - I use test fixtures or setup methods to create a consistent and known state before running tests. This helps in isolating the code under test.
5. **Use of Assertions**
    - I use assertions to check if the function returns the expected result.
6. **Automate Testing**
    - I set up automated testing pipelines that run tests automatically when code changes are pushed. Continuous Integration (CI) tool like GitHub Actions is valuable for this.
7. **Clear and concise code**
    - Best practice to make easier the understanding of my code and contribute to it.
8. **Test Documentation**
    - I document test cases, especially when they are complex or involve specific scenarios.


