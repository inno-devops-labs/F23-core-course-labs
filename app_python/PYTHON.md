# Why Flask is a Good Choice for a Time Display Application

Flask is a lightweight and flexible web framework that is well-suited for small to medium-sized web applications, such as a time display application. Some of the reasons why Flask is a good choice for this type of application include:

- Minimalistic: Flask has a minimalistic design that allowed me to focus on the core functionality of the app
- Easy to learn: Flask has a simple and intuitive API that makes it easy and fast for me to get started
- Flexible: Flask is highly customizable and allows developers to choose the components they need for their app
- Scalable: Flask can be scaled up as needed by adding more components or integrating with other tools and technologies.

# Best Practices Applied to the Web Application

To ensure that the time display application is secure, maintainable, and scalable, the following best practices were applied:

- Separation of concerns: The application was designed with a clear separation of concerns between the front-end and back-end components. The front-end uses HTML and CSS to display the time, while the back-end uses Flask to handle requests and update the time.
- Modular design: The application was divided into modular components that can be easily added or removed as needed. For example, the time display component can be swapped out for a different component without affecting the rest of the application.
- Testing: The application was thoroughly tested using unit test to ensure that it functions correctly and meets the requirements.
- Code quality: The code was written with readability, maintainability, and scalability in mind. Best practices such as descriptive variable names and consistent coding style were followed to make the code easy to understand and modify.

# Following Coding Standards and Ensuring Code Quality

To follow coding standards and ensure code quality, the following steps were taken:

- Consistent coding style: A consistent coding style was established and followed throughout the app. This included guidelines for indentation, naming conventions, and formatting.
- Linting: A linter (prettier for html) was used to catch issues before they could cause problems.
- Version control: The code was stored in a version control system such as Git, which allowed for easy collaboration and tracking of changes. This also allowed for easy rollback in case of issues or bugs.

# Unit Tests

I have created single test_main.py where I wrote several unit tests checking whether webpage loads, whether time shows and whether time changes on page refresh. I used such best practices:

- Descriptive test function names: This makes it easier to understand what each test is doing and helps with debugging.
- Keep tests independent: This helps to isolate failures and makes it easier to pinpoint the cause of a failure.
- Used fixtures to setup test data: Fixtures are functions that can be used to setup test data or state before each test runs. This can help reduce duplicated code and make tests more readable.
- Used assertions to check expected results: Assertions needed to check that the output of a function or method matches the expected result.
- Clear and concise code: This makes it easier for others to contribute to my codebase and helps with debugging.
