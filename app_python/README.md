# Python Web Application Project: Moscow Time Display

## Description

This project aims to develop a Python web application that displays the current time in Moscow. The application will provide users with an interface to view the current date and time in Moscow, which can be particularly useful for users in different time zones or anyone interested in real-time information.

## Table of Contents

- [Project Name](#project-name)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [License](#license)
  - [Author](#author)

## Installation

Provide instructions on how to install and set up your Python web project. Include any prerequisites and steps needed to get the project up and running. You can use code blocks to show commands.

```bash
# Clone the repository
git clone https://github.com/Q-Tify/core-course-labs-devops.git

# Change to the project directory
cd core-course-labs-devops
cd app_python

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On macOS and Linux:
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# To run use:
flask run

# Don't forget to export variables:
export FLASK_APP=application.app
export FLASK_ENV=development

# Also there is a pre-commit option:
pre-commit install
pre-commit run --all-files

```

## Usage
Upon accessing the application in your web browser, you will see the current date and time in Moscow displayed on the homepage.

## Features
- Display the current date and time in Moscow.
- User-friendly web interface.
- Responsive design for various devices.
- Easy-to-understand and clean user interface.

## Technologies Used
- Python: The core programming language used for the backend development.
- Flask: A lightweight and flexible web framework for building web applications in Python.
- HTML/CSS: Frontend design and structure using HTML and CSS.
- Datetime Module: Python's datetime module for handling date and time-related operations.

## Project Structure

The project structure is organized as follows:
- application/: Directory for the application.
- init.py: The starting application file.
- app.py: The main Python file for setting up the Flask application.
- routes.py: The main Python file for setting up the Flask routes.
- static/: Directory for static assets (CSS, images, etc.).
- templates/: Directory containing HTML templates.
- index.html: The HTML template for displaying the current time in Moscow.
- tests/: Directory for tests.
- venv/: Directory for virtual environment.
.gitignore: File which tells git which files to ignore.
- config.py: Configuration file for the Flask application.
- README.md: Project documentation file.
- PYTHON.md: Best practices documentation file.
- requirements.txt: List of Python packages required for the project.

## License
This project is licensed under the MIT License.

## Author
Arseniy Rubtsov