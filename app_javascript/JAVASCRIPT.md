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
