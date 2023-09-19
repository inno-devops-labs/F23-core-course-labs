# Simple Web App (Typescript version)

## Technologies used
- React.js: My favorite library for building UI.

- React Query: Great solution for client-side data fetching.

- TailwindCSS: Great CSS framework for quickly styling a website.

## Best practices

### General
- Scalable and maintainable project structure and naming conventions.
- pre-commit hooks which include linting and format-checking.
- `.prettierrc` file to ensure code-style consistency.
- Deployed version of the app to be viewed easily.
- Typescript.
- App as a submodule.

### Coding standards
- Descriptive variable names.
- Scalable folder structure.
- Separation between UI and business logic.
- Error handling.

### Testing

#### Unit Tests:
There is a total of 3 unit tests enclosing a good part of the app's functionality and UI components. They test that the components render the UI properly.

#### Best Practices
- Testing units focus on one tiny bit of functionality.
- Test units are fully independent.
- Tests run quickly.
- `vitest` to organize and run tests.
- Tests mimick what the user sees on the screen using `React Testing Library`.
- Mock prop values.
- Easy-to-follow test file structure which matches that of the app.
- 100% test coverage for tested components.
- Scripts to run unit tests and coverage reports.

### Ensuring code quality
- Pre-commit hooks will lint the code and format-check it to avoid issues further down the line and ensures that consistent code style is maintained in a collaborative environment.
- `.prettierrc` will ensure that all collaborators follow the same conventions for code style.
