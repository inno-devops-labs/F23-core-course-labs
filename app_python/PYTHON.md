# Framework

I decided to go with fastapi because this framework is super-lightweight and is very simple to use.

It mostly do not concern our app (as it is very simple) but I can describe pros of this framework as I work with it very often

### Pros
1. Validation of requests and responses
2. Built-in support of openapi and thus api page
3. Asyncronous support
4. EASY to use and extend
5. Good typing system which allows developer to maintain types across all python app
6. Support of asynchronous code

### Cons
1. Rare bugs (Once I encountered a bug that lead to memory leak but it was fixed in one of future updates)
2. Performance - it is a problem for all python apps. It is not recommended to build all your production on python :)

# Best practices
1. Code style
2. Tests
3. Typed code

## Linter and Code style
I used `pycodestyle` to follow `PEP-8` standard.

## Tests
For tests I used `pytest` and `freezegun` in order to stop time across all python (it is very useful for apps or programms dependent on time).

## Typing
I tried to explicitly set types for any possible variable and paramter as it greatly reduces number of bugs.
