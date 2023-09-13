# Moscow Time Web Application
This is a simple Python web application that displays the current time in Moscow.


## Docker  containerization and imaging
To build the image type the following in the root of the project:
`docker build -t mtime-python-app .`

To pull the image type the command:

`docker pull pavel5609/do_course:latest`

or use Docker UI app.

To run the image type:
`docker run -p 5000:5000 mtime-python-app`


## Dependencies
- Python 3.x
- Flask
- pytz

Flask is perfect production-ready framework to develop simple web applications in Python.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
