# Lab 1 - Python solution

## Researched best practices
After some time of research, I see several options here:
1. Use standard Python `http` package
pros: easy to use, Python built-in package
cons: doesn't support asynchronous requests, which can help when we have too large amounts of requests

2. Use `Django`, `Flask`, `FastApi`:
pros: easy application support, good documentation, no need to think about low level
cons: too complex for our task

3. Use `aiohttp`(https://github.com/aio-libs/aiohttp)
pros: easy to use, supports asynchronous requests
cons: too difficult to develop big web applications with it, but for our task it works

## Linters for Python and Markdown
For Python I use `black`, for Markdown VScode extension `Markdown All in One`

## Unit tests
For Unit testing I use PyTest, tests covered `time_provider.py` service