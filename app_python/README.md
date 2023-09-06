# Lab 1 - Web application - Moscow time

## Motivation
The goal of the project is to allow users see current Moscow time in a browser page.


## Description
The project is implemented using Python Flask framework. It provides one route '/' to the
main page where Moscow time is displayed. The project is tested using pytest framework.

The web application provides the following functionality:
- Display current Moscow time
- Update the time when the page refreshes


## Installation
In order to install the project one has to firstly clone the repository:  
`git clone https://github.com/vladimirKa002/devops-course-labs.git`

Then install necessary dependencies:  
`pip install flask pytz pytest`


## Usage
To run the application use the command:  
`python app_python/app.py`

To test the application use the command:  
`python -m pytest app_python/tests/`

Then open `http://127.0.0.1:5000/` in your web browser. You will see a message like as follows:  
`Current Moscow time is 2023-09-06, 08:51:18.794`


## Author
Vladimir Kalabukhov, v.kalabukhov@innopolis.university