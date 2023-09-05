## Python Web Application

#### Framework

As a web framework for python I used `Flask`. Flask is a popular web framework for Python, known for its simplicity, flexibility, and fine-grained control. It is often used to build web applications due to these reasons. Moreover, it is lightweight and highly extensible, which is important requirement to build qualitative web application. Nevertheless, it is not recommended to use it in very large web applications due to its simplicity, and sometimes it may seems that user should make too many decisions by themselves, what might be not very suitable for big projects. But for this project these problems are not threaten.

#### Best practises

There are several best practices I followed in order to build web application: 

- **Project Structure**: Organize project structure logically. Separate application into different modules based on their functionality. This keeps the codebase clean and easy to navigate.
- **Template Usage**: Use Jinja2 templates for frontend rendering. Keep logic in views and presentational aspects in templates.
- **Testing**: Write tests for application. Tests can help to catch bugs and ensure code works as expected.
- **Keep code clean**: It is important to keep codebase clean, do not use too big function. If necessary it is reasonable to split code into several logical modules.
- **Regularly use linter**: That will lead to enforcing code standards in project, catch some errors in early stage and keep code clean.

As a testing framework was used `pytest` due its simplicity and popularity. 
As a linter was used `pylint` as a standard linter for python.