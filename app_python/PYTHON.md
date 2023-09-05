## Task 1: Python Web Application

### Framework selection:

  I've chosen Flak since it's the most popular framework for two last years ([source](https://www.jetbrains.com/lp/devecosystem-2022/python/)).

  Useful features of Flask affected my choice:

  - Lightweight and minimalist
  - Easy to learn and use
  - Modular designed framework
  - Built-in dev server
  - It's open source product
  - Unit testing support

### Implemented best practices and followed code standards:

  - Proper naming of endpoints 

    `/time` - noun. And GET HTTP method stands for action name. No any verbs in endpoint name
  - Using proper project structure:
    ``` 
    /api
      /model
        time.py
      /route
        time.py
      /schema
        time.py
      /service
        time.py
    ```
  - Blueprints usage, which gives modularity of the application
  - Use Marshmallow for serializing objects
  - Use auto-swagger library
  - Document the API

### Ensured quality
  - via unit tests (`/test`)
  - via manual testing
  - via `flake8`
  - via cspell
  - via python extensions in IDE
