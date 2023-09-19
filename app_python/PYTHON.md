# Python part description

### Arhitecture

First of all, to start develop we need to identify key parts of an architecture. 
For this project I took ideas of Onion-Arhitecture and Microservices. 

This choice gives a strict separation between logical parts of an application 
**(user-side, server-side, interfaces and business-logic)**. 
Using that idea we can with low effort scale our application code base in future and 
also make changes in one part without risk to "damage" others. 
Moreover, it will be much easier to test it as it is possible to mock entire layer and integrate it with operational parts of implementation

In this particular approach I now have separation for `web` and `domain`, 
excluding _service part_ as I don't need to prepare data from queries to operate inside domain (and transform data for responses). 
But if it will some variants inside web application to use service layer in the future app modification, I would add that layer easily.


### Part 2: Code
During development, I tried to follow SOLID practices, and architecture I have picked almost ensures it.

My code used formatting on commits (via `pre-commit`) with black, flake8 to follow PEP8. 
To reduce code-reading problems and improving code quality I also install IDE static code analyzers (sonarlint, flake8, pylint).

Also, I have used some kind of "philosophy" for programming: typed python - 
there are type hints&annotations in code and type checking.

### Framework choice
I have considered several the most popular frameworks: `Django`, `Flask`, `aiohttp`, `FastAPI`. It is easy to find docs and manuals for one of them.

I would like to use async framework to increase performance. So `Flask` don't suit this parameter. 
Also, its async "little brother" `quart` has bad number of RPS due to some benchmarks.

`Django` - not suitable for this kind of project: too heavy and complex.

`FastAPI` has a good community, docs, performance, but I have chose **aiohttp** because it is lighter and stable.


### Code testing 
1. For testing, I have used unit testing, for such small application 1 test was enough
2. I have applied range-act-assert approach for my tests
3. My test checking that route returns status code of success and then checking that time actually changes by making two consequent requests to Test Server with real handler
### Docker

For containerizing app I copied requirements file and established environment with all dependencies, then I have copied source files and executed my application
- to build project from you should run following inside app_python directory:
        
        docker build ./

- to pull project run:

        docker pull dashvayet/lab2_app_python:latest

- to run project:
  
      docker run -ti -p <port to open from host machine>:5000 dashvayet/lab2_app_python:latest


