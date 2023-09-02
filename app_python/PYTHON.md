# Python Flask

The application is built using flask framework. Here are main reasons why I have used this framework specifically:

- Flask is a micro-framework, which means it comes with minimal features out-of-the-box and it is very easy to quickly set up a project and get started.
- Flask has a modular design and is highly extensible with a wide range of extensions and third-party libraries available. This allows developers to add complex functionalities, like authentication, databases, and forms, to their application without rewriting the core functionality from scratch.
- Flask has excellent documentation which is well-organized and easy to follow.
- Flask is well-suited for creating RESTful APIs, which makes it a popular choice for backend development for mobile and web applications.

## Implementation details
* I have utilized Flask's standard approaches for organizing the project files, dividing the project into blueprints, and converting the entire project into a Python package, which can then be installed as a library. 
* Since the project is currently quite simple, HTML documents are rendered on the server-side. 
* The `pytest` library is used for testing. I chose `pytest` over `unittest` primarily for its simplicity and extensibility. Currently, there is only one file, `test_app.py`, which contains a single function that makes a GET request to verify whether the server time matches the current time.
* The `pylint` library is utilized to analyze the code, verifying compliance with coding standards and error-free syntax, while also enforcing the PEP 8 coding style.

## Project Structure
The structure is quite simple at the moment, but as time passes and development continues, it will become more complex

```
app_python
├── app/
│   ├── __init__.py
│   ├── views/
│   │   ├── __init__.py
|   |   └── time_view.py
|   └── templates/
│       └── current_time.html
├── tests/
│   ├── __init__.py
|   └── test_app.py
|
├── run.py
└── requirements.txt
```

### Files and Directories

- `app/__init__.py`: Initializes the Flask application.
- `app/views/`: Contains files handling the view (routing) layer of the application.
- `app/templates/`: Contains the HTML templates to be rendered in the application.
- `tests/`: Contains test files for the application 
- `run.py`: Entry point for starting the application.
- `requirements.txt`: Contains the Python package dependencies of the project.


