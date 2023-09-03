# Moscow Time Display Web App

This is a simple Flask web application that displays the current Moscow time.
The application updates the time every second without requiring a page refresh.


## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)

## Features

- Displays the current Moscow time.
- Updates the time every second using JavaScript.
- Use tools for dependencies or at least `requirements.txt` file for Python packages.
- Work with docker
- Use `.gitignore` file to exclude not relevant files from the git.
- Can save address and time for every connection in file `visits.txt`

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (3.6 or higher)
- Flask (`pip install flask`)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/PlutoEx/DevOps-course-labs.git
   cd app_python

2. Install dependencies:

   ```sh 
   pip install -r requirements.txt
   
### Usage

1. Run the flask app:
   
   ```sh
   python -m venv .venv
   .venv/Scripts/Activate
   flask run

2. Enter the app in browser at: http://127.0.0.1:5000/

### Tests

* I add test to check moscow time

* To run it:

   ```sh
  python -m unittest tests.py