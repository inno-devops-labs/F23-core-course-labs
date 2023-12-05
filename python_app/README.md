# Moscow Time Web Application

This is a simple Python Web Application that displays the current Moscow time. </br>
The application is built using the Flask framework.

## Features
- the website displays the current Moscow time. 
- the time is updated upon refreshing the webpage.

## Installation

1. Clone the repository: `git clone https://github.com/quhaaST/core-course-labs/tree/main/python_app`
2. Change into the project directory: `cd python_app`
3. Install dependencies: pip install -r requirements.txt

## Usage

1. Run the Flask development server: python app.py
2. Open your web browser and navigate to http://localhost:5000
3. You should see the current Moscow time displayed on the webpage
4. Refresh the webpage to update the displayed time
5. To check the amount of visits of the website navigate to `/visits` path from the main web-page.

## Docker usage

### How to build
```
docker build -t evalekalek/devops:latest .
```

### How to pull
```
docker pull evalekalek/devops:latest
```

### How to run
```
docker run -it --rm evalekalek/devops:latest
```

## Testing
There are several tests to provide the correct functionality in `tests/test.py`. </br>
To run the tests use `python -m unittest tests/test.py`.

## CI/CD
![python-app workflow badge](https://github.com/quhaaST/core-course-labs/actions/workflows/python-app-workflow.yaml/badge.svg) 

As a CI tool a GitHub Actions were used. </br>
The workflow, which includes linting, testing, pushing the updated Docker image to DockerHub, will be triggered upon
any change in `python_app` folder.

## Dependencies

- Flask==2.0.1
- pytz==2021.3
- pylint==2.17.5