I used Flask, a lightweight and easy-to-use Python web framework, for this small web app. Flask is suitable for this purpose because it has built-in support for handling HTTP requests and does not require a separate HTML template.

Since we only need to print the current time in Moscow as plain text, I used the strftime function to format the output as a string. This eliminates the need for an HTML template, reducing the overall project complexity.

For testing, I used the pytest framework and pytest-flask plugin, which provides useful fixtures for testing Flask apps. Pytest is a popular choice for Python testing due to its simplicity and extensive functionality. Its ease of use makes it ideal for testing this small web app.