### Choosing of python framework

* **Django** -
  it's good enough for big projects which will be needed scaling in the future.
  But for our case - it's too overloaded

* **FastAPI** -
  it's fullstack framework designed for building APIs.
  It supports asynchronous code out of the box and aimed
  for high-performance real-time API with minimal code. Also it has automatic
  data validation and documentation

* **Flask** -
  it's micro-framework designed for building web applications and APIs.
  It has a high degree of customization and flexibility. The main cons is
  large community and ecosystem

For this app I decided to choose FastAPI due to its performance and conciseness  

### Best practises
* **Consistent & predictable project structure** ([source](https://github.com/zhanymkanov/fastapi-best-practices#1-project-structure-consistent--predictable))
* **REST API** - for getting date we use HTTP GET request with clear endpoint
* **PEP 8** - style guide for python code. I use PyCharm suggestions and auto-formatting
* **.gitingore** - commit only crucial elements of repository
* **Autotest** - run all unit tests during build to minimize bug search time. For writing and run tests I use pytest

### Coding standards
* Implemented autotests using pytest
* Virtual environment to isolate all dependencies
* Use PEP 8 integrated into PyCharm
* Use pre-hook for formatting code. I use [black](https://pypi.org/project/black/)