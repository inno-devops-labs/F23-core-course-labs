# App python

## Framework

I chose FastAPI for this application for several reasons:

- **Lightweight** of the framework: FastAPI is much simpler than Django
and has more features than Flask.
- **Async Support**: FastAPI fully supports asynchronous programming, 
that allows you to handle concurrent operations.
- **Scalability**: This framework provides a solid foundation for future scalability.
- **Automatic Documentation**: FastAPI automatically generates OpenAPI documentation (Swagger).

## Best practices

1. **Project structure**

    FastAPI has its own suggestions for project structure. I've applied [this](https://github.com/zhanymkanov/fastapi-best-practices)
best practises for project structure.

1. **Tests**

    Asynchronous tests using pytest to check time updates every time you refresh the page.

1. **Environment management**
   
    Use environment to control timezone of time to show.

1. **Async endpoints**

   Utilize asynchronous programming with `async` to improve application responsiveness.

1. **Dependency injection**

   As part of project structure, dependencies are separated by files in `requirements` folder.
