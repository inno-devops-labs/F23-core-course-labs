# Moscow Time Web Application
This is a simple Python web application that displays the current time in Moscow.

## Dependencies
- Python 3.x
- Flask
- pytz

Flask is perfect production-ready framework to develop simple web applications in Python.


### Docker

#### How to build?

Run the following command to build the docker image:  
`docker build -t app_python .`

#### How to pull?

In order to pull the Docker container image run this command:  
`docker pull pavel5609/do_course`

#### How to Run?

You can run the application using the following command:  
`docker run -p 5000:5000 pavel5609/do_course`

The application will be accessible via the following link: `http://localhost:5000/`


## Unit Tests

To test the application use the following command which will invoke pytest:  
`python -m pytest`


## Author
Pavel Bakharuev, p.baharuev@innopolis.university