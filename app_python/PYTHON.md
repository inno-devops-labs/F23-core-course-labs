For this task I decided to use the "Flask" framework since it is one of the most popular python frameworks and allows to quickly create a simple web application with basic features like routing and html templates.

Prerequisites: install flask with "pip3 install Flask"

run local server with "sh dev.sh"

## Unit test
In order to verify that our application receives the actual moscow time, I get moscow time from its timezone(using `pytz` library). These 2 functions get called and then the result from application function is compared with time from the `pytz` timezone.