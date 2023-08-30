# Website


# Framework Mosh Pit
There are multilpe *frameworks* to choose from:
- **Django** - a highly abstracted full-stack framework. It is robust and secure, but way too bulky for such a simple app. I already worked with Django, and I want to try something new.
- **Flask** - a microframework that still nontheless provides all the necessary components for a simple app: URL routing, request handling, session management, testing. Also, I want to try it :)
- There are many other *frameworks*, but they are much less popular and therefore have less support and project (therefore less training data for ChatGPT, which is problematic, since I already forgot how to write code myself).

So, I decided on using **Flask**, since it provides all the necessary abstraction for quickly writing a simple website while staying relatively light-weight.

# Best Practices/Standards
Standards I followed:
- The **PEP8** standard.  
- Type hinting.

To ensure code quality and standard compliance:
- **Pylint** was used for style linting, static error analysis, code smells (error in screenshot just as example, I fixed it).  
![image](/home/tea/Documents/inno5/DOE/DOE-course-labs/app_python/resources/S_2023-08-31_00-15-08.png)
- **Mypy** for static type checking.  
![image](/home/tea/Documents/inno5/DOE/DOE-course-labs/app_python/resources/S_2023-08-31_00-23-58.png)
- **Black** (a python formatter) for code formatting.

I, of course, also installed the mypy, pylint and black plugins for my editor for faster feedback.

# Testing
I wrote a simple test case (test.py) using Flask testing capabilities and the unittest library.  
The test checks that "Moscow" is mentioned in the web server response and that the responses are different of requested at different times.
