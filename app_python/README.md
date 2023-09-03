# Python Web Application Development - Daniil Okrug

The application displays Moscow time. In this project I used Flask framework because of its convenience and simplicity in web application development.

The main file is app.py which contains routes '/' and '/time'. First route renders index.html page with Moscow time. Second route provides time in Moscow timezone.

The project has a templates folder that contains HTML pages to render on the client side.

For testing and determining the percentage of test coverage pytest and pytest-cov are used. All tests are now in the tests folder. 
