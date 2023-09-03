### FastAPI application for DevOps course.
I chose FastAPI framework, because it has high performance, asynchronous capabilities (that make it efficient to handle big number of simultaneous requests, it's beneficial for such applications as this, because it requires real-time data processing). As an advantage, it has automatic API documentation generation.

In variable app I created a new instance of the FastAPI framework, it will be used to define routes, endpoints and behavior of web application.

In next statement I declare an instance of Jinja2Templates, that used for rendering HTML templates.

In next lines I defined an endpoint using @app.get decorator, it configured to handle HTTP GET requests to the root 'http://{host}:{port}/'. It returns current Moscow time as an HTML page response.

I used current time on server with specified timezone as an information about current Moscow time. This application will work correctly with assumption that server obtains correct information about current time.

I tried my best in code style, I don't know if I need to clarify something about it.

I created a config file temporary, for containing some useful data. It will be removed on stage of containerization.
