# Simple Web App

## Technologies used
- Flask: A lightweight Python web framework. A perfect option for a simple app such as this one since it's easy to set-up and the base app is 5 lines of code.

- datetime: Python's built-in module for working with dates and times. Straightforward, easy-to-use.

## Best practices

### General
The project follows a simple structure fitting of its simple nature, some basic best practices were applied to the project including:
- `requirements.txt` file to set-up a virtual environment (instructions below) to ensure the app's portability.
- Conventional commits are adhered to across the repository.
- `.gitignore` file. No need to explain this one.
- `main` branch is protected from direct pushes.
- pre-commit hooks were set-up for the project *NOT THE REPO*, they're not active at the moment (not in `.git`) since the repo will contain 2 projects.
- Documentation with instructions to run the app.

### Coding standards
- Descriptive variable names.
- Comments.

### Testing

#### Unit Tests:
There is a total of 2 unit tests enclosing the full functionality of the app:
- Health check - checks that the server is running
- Time check - checks that the server displays the correct time

#### Best Practices
- Testing units focus on one tiny bit of functionality.
- Test units are fully independent.
- Tests run fast
- `pytest` to organize and run tests.
- Test modules to organize tests (would be useful in a larger project context)
- 100% test coverage.

### Ensuring code quality
- Pre-commit hooks will use `black` formatter on all python files in the project. They will also ensure an empty line in the end of a file and remove any trailing whitespaces from code.
