## Why I chose FastAPI:

FastAPI is an innovative web framework tailored for building APIs with Python. I selected it for the following reasons:

- **speed**: rooted in Starlette and Pydantic, FastAPI outpaces many of its counterparts; in some benchmarks, it surpasses Flask and Django,


- **ease of use**: FastAPI's syntax is concise, and it provides automatic interactive API documentation,


- **type annotations**: one of the unique features of FastAPI is its use of Python type annotations,


- **asynchronous support**: FastAPI fully supports asynchronous request handlers; this allows it to manage a high number of concurrent connections with fewer processes and threads.

### Pros of FastAPI:
- fast: one of the fastest frameworks for Python,
- type checks: uses Python type hints,
- automatic interactive API documentation.

### Cons:
- newer framework: it might not have as extensive a community as Flask or Django.

## Linters used:
- for Python: `flake8`
- for Markdown: `markdownlint`

### To run the linters:
- `flake8 main.py`
- `markdownlint README.md`

## Best practices that I applied:

- **consistent timezone management**: instead of depending on the system's timezone, which can introduce inconsistencies, I purposefully utilized the Moscow timezone through the `pytz` library,


- **separation of concerns**: the core application logic is distinct from the framework and routing logic, promoting modularity,


- **code modularity**: the application's structure allows for easy future extensions or modifications,


- **testing**: I used `TestClient` which is built into FastAPI, simplifying the testing process for endpoints and ensuring the application functions as anticipated.


## Following coding standards:

- **descriptive function names**: function names such as `display_msk_time` allow to understand what this function is intended to do,
  
- **use of libraries**: the integration of the `pytz` library guarantees accurate timezone information,

- **explicit imports**: rather than choosing wildcard imports (like `from datetime import *`), specific modules and functionalities are imported,

- **consistency**: throughout the codebase, a uniform style is maintained regarding naming, spacing, and structuring.

## Implementing testing:

### Test steps:

- **initial request**:
The test begins by making a GET request to the root endpoint (/).
It expects a successful response with a status code of 200.
The response should contain the current time in Moscow.
- **wait**:
The test then waits for 2 seconds using the time.sleep(2) function.
This pause ensures that there's a noticeable difference in time between the two requests.
- **second request**:
After the wait, another GET request is made to the root endpoint (/).
Again, a successful response with a status code of 200 is expected.
The response should contain the updated current time in Moscow.
- **assertion**:
The test finally checks that the Moscow time received in the first response is not equal to the time received in the second response.
This assertion ensures that the time is updating as expected.

### Best practices applied:
- **modularity**: the test is written as a function, making it modular and easy to integrate with testing frameworks like pytest.
- **assertive testing**: it uses assertions to ensure that the responses from the API are as expected. This includes checking the status code and the content of the response.
- **time-based testing**: by introducing a delay between requests and then comparing the results, the test ensures that the time functionality of the application is working correctly.
- **dependency isolation**: the test uses TestClient from fastapi.testclient to simulate requests to the FastAPI application. This means the test doesn't rely on an external server or environment to run, ensuring consistency and reliability.
- **descriptive variable names**: variables like response1_time and response2_time are named descriptively, making the test easy to read and understand.

## Ensuring code quality:

- **simplicity**: the code remains concise, focusing solely on the required task,

- **error handling**: by default, FastAPI administers error handling, ensuring that errors are met with clear and informative messages,

- **deterministic timezone management**: the adoption of the `pytz` library for timezone management ensures consistent behavior across diverse systems and environments - without such measures, varying servers might misinterpret "now" based on their system configurations,

- **automated testing**: automated tests ensure the main application functionality operates as anticipated.
