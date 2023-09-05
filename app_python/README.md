# Display Current Time in Moscow

Hi :wave:, this is a simple app's repository that displays the current time in Moscow.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Linter, Auto Formatter](#linter-auto-formatter)

## About

This app displays the current time in Moscow. It was created for educational purposes upon request during a DevOps course.

## Features

List the key features of your app.

- Display Time in Moscow

## Getting Started

### Prerequisites

#### Create a Virtual Environment
```Bash
python3 -m venv myenv
```
#### Activate the Virtual Environment
- On Windows
```Bash
myenv\Scripts\activate
```
- On macOS and Linux:
```Bash
source myenv/bin/activate
```

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
3. Install dependencies: 
```Bash
pip install -r requirements.txt
```

## Usage

To run the app use the following command:
```Bash
python3 app.py
```

It should run on localhost: http://127.0.0.1:5000/

## Tests
To run tests, execute the following command: 
```Bash
python3 -m pytest
```

## Linter, Auto Formatter
To run linter and auto formatter execute the following command: 
```Bash
pre-commit run --all-files
```
