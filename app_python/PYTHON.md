# Explanation of decisions

## Starlette as a server framework
Starlette is a simple lightweight framework for web applications.

At the beginning I wanted to use FastAPI, but realized that most of major features (like pydantic support, etc.) is unnecessary for this particular educational project. As the result I decided to use Starlette which is a base for FastAPI itself.

Another pros:
- Developer of the project like the simplicity of Starlette comparing to Flask, Django and others
- [It's fast](https://www.techempower.com/benchmarks/#hw=ph&test=fortune&l=zijzen-sf&section=data-r20)

## Uvicorn as ASGI
For this particular project there is no any limitations in choose of ASGI, just support the spec. So I decided to use Uvicorn as [the fastest one](https://www.techempower.com/benchmarks/#hw=ph&test=fortune&l=zijzen-sf&section=data-r20)

## Pylint as a linter
Pylint is one of the oldest tools for Python and proven by the time. We need it to check if our code is PEP8-complaint

## Pytest as a unit test runne
Pytest is standart de-facto for unit testing in python. In my unit test I covered the ability of `get_time` function to produce correct output for different time zones
