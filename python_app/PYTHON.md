### Framework selection
As for the framework to work with, I have chosen Flask. </br>
The Web App hides a very simple logic, containing only 1 route. Due to these facts the choice was made in 
favor of Flask, as it provides all the necessary mechanics to fulfill the requirements. </br>

For example, Django is a more powerful Web App creation framework. 
However, it is too excessive for this kind of the task. 

Moreover, there are no problems with testing the Web App created with Flask.

### Best practises and code quality
There were several practises applied to the project:
- the codebase is modular, separating source code, tests, templates and styles
- the implemented code is in simple and readable manner, following PEP8 standards
- testcases cover all the requested features of the website

### Testing 
There is `TimeZonedTimeTestCase` as the testing class, which is written with Python `unittest` library. </br>

The logic behind the tests is simple, while covering all the required scenarios, such as:
- the website is loading and displays the correct time
- refreshing the website triggers changing the displayed time