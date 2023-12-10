# Best practices

## Project Structure:

- Organize your project into logical directories, such as `lib/`, `bin/`, `test/`, and `config/`.
- Use packages and dependencies wisely to structure your codebase.

## Dependency Management:

- Use the `pubspec.yaml` file to manage dependencies.
- Keep your dependencies up to date and use the latest versions whenever possible.

## API Documentation:

- Document your API endpoints using tools like Swagger or OpenAPI.
- Generate and maintain API documentation to make it easier for others to use your backend.

## Code Style and Formatting:

- Follow the Dart code style guidelines, which can be enforced using tools like `dartfmt`.
- Use meaningful variable and function names to improve code readability.

## Testing:

- Write unit tests and integration tests for your code using the test package.
- Use tools like `mockito` for mocking dependencies in your tests.

# Production ready frameworks

There are several server frameworks available for Dart to help developers build efficient and scalable server-side applications

## Aqueduct:

Aqueduct is a powerful Dart framework for building RESTful APIs and web applications. It focuses on features like authentication, database ORM (Object-Relational Mapping), and more.

## Angel:

Angel is a full-featured, highly extensible server framework for Dart. It supports various types of applications, including RESTful APIs, real-time applications, and MVC web apps. It comes with a variety of plugins for added functionality.

## Jaguar:

Jaguar is a flexible, high-performance web framework for Dart. It provides tools for building RESTful APIs and web applications with a focus on speed and efficiency.

# In this project

I decided to use Jaguar because of it simplicity and rich features.
