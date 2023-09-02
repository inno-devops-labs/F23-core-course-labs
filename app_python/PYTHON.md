## Choosing framework
When choosing a suitable web framework for this project, key factor was the **performance**, because the application is real-time and needs to show up-to-date time to users.
The second factor is the **simplicity** of writing code and a non-overloaded project structure suitable for a small project like this.
An additional plus will be the presence of built-in **testing** and features like automatic generation of OpenAPI documentation.

Here is perfomance comparison based on [benchmark](https://github.com/klen/py-frameworks-bench):

| Framework | Requests/sec | Latency 50% (ms) | Latency 75% (ms) | Latency Avg (ms) |
| --------- | -----------: | ---------------: | ---------------: | ---------------: |
| [blacksheep](https://pypi.org/project/blacksheep/) `1.2.5` | 18546 | 2.80 | 4.53 | 3.41
| [muffin](https://pypi.org/project/muffin/) `0.87.0` | 16571 | 3.09 | 5.17 | 3.83
| [sanic](https://pypi.org/project/sanic/) `21.12.1` | 15558 | 4.70 | 5.14 | 4.08
| [falcon](https://pypi.org/project/falcon/) `3.0.1` | 15554 | 3.29 | 5.49 | 4.08
| [baize](https://pypi.org/project/baize/) `0.15.0` | 13880 | 3.69 | 6.21 | 4.58
| [starlette](https://pypi.org/project/starlette/) `0.17.1` | 13797 | 3.70 | 6.16 | 4.60
| [emmett](https://pypi.org/project/emmett/) `2.4.5` | 13380 | 5.54 | 6.10 | 4.75
| [fastapi](https://pypi.org/project/fastapi/) `0.75.0` | 9060 | 5.46 | 9.79 | 7.03
| [aiohttp](https://pypi.org/project/aiohttp/) `3.8.1` | 7240 | 8.74 | 9.01 | 8.84
| [quart](https://pypi.org/project/quart/) `0.16.3` | 3425 | 18.99 | 20.08 | 18.68
| [tornado](https://pypi.org/project/tornado/) `6.1` | 3232 | 19.76 | 19.94 | 19.81
| [django](https://pypi.org/project/django/) `4.0.3` | 1002 | 59.00 | 66.26 | 63.72

We see no Flask in this table because it is not async.

The choice fell on [BlackSheep](https://pypi.org/project/blacksheep/) because it is the fastest framework in this comparison, and it has a simple and intuitive structure like Flask or FastAPI. It has testing integration, OpenAPI docs generation, authentication, and other useful features from the box.

## Best practices used
- Project overall structure based on official [BlackSheep MVC project template](https://www.neoteroi.dev/blacksheep/mvc-project-template/).
- Added [OpenAPI](https://swagger.io/specification/) documentation generation.
- Added [pre-commit](https://pre-commit.com/) hooks to check code formatting before commit. It uses:
    - [bandit](https://github.com/PyCQA/bandit) to check for common security issues in Python code.
    - [flake8](https://github.com/PyCQA/flake8) to check for PEP8 violations and other common issues.
    - [black](https://github.com/psf/black) to format code according to PEP8.
    - [isort](https://github.com/pycqa/isort) to sort imports.
    - Used single configuration file `pyproject.toml` for this tools.
- Added [pytest](https://docs.pytest.org/en/6.2.x/) test to check application functionality.
- Requirements are split into `requirements-base.txt` and `requirements-dev.txt` to separate production and development dependencies.
- Added `gitignore` file to exclude unnecessary files from git.
