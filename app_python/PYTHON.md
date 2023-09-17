# Project information

## Best practices used
Some of the best practices list was taken from this [site](https://www.codingdojo.com/blog/python-best-practices).
1. Follow the PEP 8 Style Guide for Python Code.
2. Use Python 3 Instead of Python 2.
3. Document and Comment Your Code Properly. Example: The project has three properly documented tests.
4. Write Readable Code.
5. Use One Statement of Code per Line.
6. Use Virtual Environments.
7. Test Your Code. Example: The project has three properly documented tests.
8. Use logging. Flask provides logging HTTP requests automatically. 
9. Keep in mind The Zen of Python.
10. Keep the unified file structure.
Example: `src/app.py`, `tests/test_app.py`.
11. Use `.editorconfig` to keep code style unified.
12. Use  `.gitignore` to keep project files clean.
13. Use `requirements.txt` with the list of all used Python modules.
14. Use code formatter in `pre-commit` git hook. I have used `black` formatter.
15. Use code checker in `pre-commit` git hook. I have used `flake` checker.
16. Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit naming.

## Linter
I have used code formatter (`black`) and checker (`flake`) instead of linter.
They run before commit with thanks to Git `pre-commit` hook and Python `pre-commit` module.
The description of executable used in `pre-commit` hook is in the file `./pre-commit-config.yaml`.

## Framework selection

I have used Flask production framework.

Flask is a simple and intuitive framework for creating web applications in Python.
It supports scaling, error handling, and database management.

### Applied advantages
* The Flask framework is easy to understand.
I have never ever written Python web applications and for me this advantage was the key one.
* Testing.
Using Flask for web development allows for unit testing through its integrated support, built-in development server, fast debugger, and restful request dispatching.
It is lightweight to enable you to transit into a web framework easily with some extension.
* Logging. Flask provides logging HTTP requests. 

### Disadvantages

#### Scalability
Another issue about flask is that it has a singular source which means that it will handle every request in turns, one at a time.
So if you are trying to serve multiple requests, it will take more time.
With fewer tools at your disposal, you may need to install more modules.
This could be mitigated by using Python specialized hosting.

#### Modules
Using more modules is seen as a third party involvement which could be a major breach in security.
The process and development is no longer between the web framework and the developer, because of the involvement of other modules.
That could increase the security risk if a malicious module is included.


