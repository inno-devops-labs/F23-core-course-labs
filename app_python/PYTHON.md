# Lab 1
## Framework 

I had experience with Flask and Fast Api so I choose between them.
- FastAPI is designed for building APIs, while Flask can be used for building web applications and APIs. FastAPI is faster than Flask due to its asynchronous code and type annotations.
- FastAPI has automatic data validation and documentation, while Flask requires manual validation and documentation.

Start server:
```
uvicorn src.main:app --reload
```

## Best practices:
- PEP8 standarts - The code is developed in accordance with the PEP8 standards, so it will be easier for developers to perceive it
- There are tests in this project to make sure it works as planned

## Unit Tests
For testing I used **pytest** framework:

Tests:
- Check that time is updating
- Check responce code
- Check String matching
```
python3 -m pytest test_main.py
```
