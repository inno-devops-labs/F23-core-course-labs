# Display Current Time in Moscow

Hi :wave:, this is a simple app's repository that displays the current time in Moscow.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Unit Tests](#unit-tests)
- [Linter, Auto Formatter](#linter-auto-formatter)

## About

---------------------------------------------------------------


This app displays the current time in Moscow. It was created for educational purposes upon request during a DevOps course.

## Features

---------------------------------------------------------------


List the key features of your app.

- Display Time in Moscow

## Getting Started

---------------------------------------------------------------

### Installation

Provide step-by-step instructions for installing your app.

1. Clone the repository: 
```Bash
git clone https://github.com/aibek99/core-course-labs.git
```
2. Navigate to the project directory: 
```Bash
cd ./core-course-labs/app_python
```
3. Create a Virtual Environment
```Bash
python3 -m venv myenv
```
4. Activate the Virtual Environment
- On Windows
```Bash
myenv\Scripts\activate
```
- On macOS and Linux:
```Bash
source myenv/bin/activate
```
5. Install dependencies: 
```Bash
pip install -r requirements.txt
```

## Usage

---------------------------------------------------------------


To run the app use the following command:
```Bash
python3 app.py
```

It should run on localhost: http://127.0.0.1:5000/

## Unit Tests

---------------------------------------------------------------

To run tests, execute the following command: 
```Bash
python3 -m pytest
```

## Linter, Auto Formatter

---------------------------------------------------------------

To run linter and auto formatter execute the following command: 
```Bash
pre-commit run --all-files
```

## Docker 

---------------------------------------------------------------

To build the image run the following command: 
```Bash
sudo docker build -t flaskapp:1.0 .
```

To run it, use the following command:
```Bash
docker run -d -p 5000:5000 flaskapp:1.0
```

To pull it from Docker Registry:
```Bash
docker pull aibekbakirov/devops_lab2:1.0
```

To run it, use the following command:
```Bash
docker run -d -p 5000:5000 aibekbakirov/devops_lab2:1.0
```

link: http://localhost:5000/

## CI workflow

---------------------------------------------------------------

### Steps: 
- Environment Setup and Dependency Caching
- Python Dependency Installation and Security Scanning
- Code Linting and Testing
- Docker Login
- Docker Build and Push