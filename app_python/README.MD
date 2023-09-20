# Moscow Time Flask Web App

![Python CI Workflow](https://github.com/eukuz/devops-course-labs/workflows/Python%20CI%20Workflow/badge.svg)

A simple Flask-based web application that displays the current Moscow time upon page refresh.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Test](#test)
6. [Logging](#logging)
7. [Docker Usage](#docker-usage)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will guide you through the process of setting up the Moscow Time Flask app on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7+
- `pip` for package management

### Installation

1. **Clone the repository**:

2. **Navigate to the project directory**:

3. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```
   
## Usage

To run the Moscow Time Flask web app:

1. **Activate the virtual environment if not already active**.

2. **Run the app**:
    ```bash
    python app.py
    ```

3. **Open a web browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

## Test
1. Activate the virtual environment if not already active.

2. Run the tests:

```bash
python test_app.py
```

## Logging

Logs are written both to the console and to `app.log` in the root directory. The logs contain information about app events, any encountered issues, and their timestamps.

## Docker Usage

### How to Build?

To build the Docker image, navigate to the directory containing the `Dockerfile` and execute the following command:

```bash
docker build -t app_python .
```

### How to Pull?

You can pull the image using the following command:

```bash
pull eukuz/devops_course_python_app
```

### How to Run?

To run the Docker container from the image:

```bash
docker run -p 5000:5000 eukuz/devops_course_python_app 
```

After executing this command, you can access the application via `http://127.0.0.1:5000` in your browser.


## Contributing

If you wish to contribute, please fork the repository and use a feature branch.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The Flask framework for making web development seamless.
- `pytz` for handling timezones with ease.
