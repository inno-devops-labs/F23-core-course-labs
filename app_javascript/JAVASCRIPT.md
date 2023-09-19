### Justification of the flask framework:

I chose Express.js for my web app because it's like using a simple and helpful toolbox. It makes it easy to create different parts of the website and manage how people see and interact with it. Express.js is popular, like a favorite video game with lots of players, so it has lots of fans who share their tricks and tips. Plus, it can be customized easily if I want to add more things to my website later. Overall, it's like the perfect tool for building a basic website without making things too complicated.

### Best practices:

1. **Project Structure**
    - The project followed a well-organized structure, separating static assets (HTML, CSS, JavaScript) into a dedicated public folder and keeping server-related code in a separate app.js file. This separation helps in maintaining a clean and understandable codebase.

2. **Dependencies management**
    - Dependencies were managed using npm, which is a standard practice in Node.js development. The package.json file was used to document project dependencies and configuration.

3. **Middleware Usage**
    - Express.js middleware was utilized for serving static files, enhancing security, and handling HTTP requests. This promotes code modularity and reusability.

4. **ESLint**
    - ESLint is a JavaScript code analysis tool that checks your code for errors, enforces coding style conventions, and promotes code quality by providing feedback on potential issues and suggesting improvements.

        ```
        npm run lint
        npx eslint --fix .
        ```

5. **Tests**
    - Using Mocha and Chai for Unit Testing.

6. **Pre-commit**
    -   ```
        npm run precommit
        ```


### Code testing best practices:

In my javascript application in /tests/test.js I created tests for checking if my created function returns the quote of string type, if using my api I get a string and status 200 and if my service can shutdown gracefully with status 500 after pressing ctrl+c.  

1. **Test Early and Continuously**
    - I created tests in the first lab and appended them in this lab. I also run tests always before in the pre-commit.
2. **Use Descriptive Test Names**
    - I write clear and descriptive test names that convey the purpose and expected behavior of the test.
3. **Keep Tests Independent**
    - In my application each test is independent and does not rely on the state or outcome of other tests. Tests should not have hidden dependencies.
4. **Automate Testing**
    - I set up automated testing pipelines that run tests automatically when code changes are pushed. Continuous Integration (CI) tool like GitHub Actions is valuable for this.
5. **Clear and concise code**
    - Best practice to make easier the understanding of my code and contribute to it.
6. **Test Documentation**
    - I document test cases, especially when they are complex or involve specific scenarios.
7. **Include Positive and Negative Tests**
    - I test both expected (positive) and unexpected (negative) scenarios to ensure robust error handling and fail-safes.
8. **Use of Expect Statements**
    - Expect statements should be used for checking that the code is behaving as expected. These statements can encompass tasks such as verifying the presence of specific elements on the page, confirming the invocation of particular functions, or validating the return of expected values.
