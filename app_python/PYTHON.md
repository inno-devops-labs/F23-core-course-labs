## Choice of framework


I chose ``Flask`` for this project due to following reasons:
 - It is well-suited for small projects:)
 - It is easy to insert content into HTML templates using it.
 - It has build-in development server for testing.

## Best practices

- Logging: use ``logging`` library for printing logs into ``app.log`` file
- ``.gitignore``: use it to stash logs.
- Error handling: add ``error.html`` template to render it in case of errors.
- Code formatting: use ``Pylint`` for it.
- Testing: wrote test for validating if rendered time is correct using ``unittest`` library.
- Created ``requirements.txt`` file using <code>pip freeze > requirements.txt</code> command.
- Store all HTML templates into separate folder ``templates``