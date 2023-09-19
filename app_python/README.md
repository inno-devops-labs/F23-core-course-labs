[![CI](https://github.com/Wild-Queue/devops-core-course-labs/actions/workflows/tests.yml/badge.svg?event=push)](https://github.com/Wild-Queue/devops-core-course-labs/actions/workflows/tests.yml)
# Time Server

A simple HTTP server that displays the current time in Moscow.

### How to Run

1. Make sure you have Python installed on your machine.
2. Open a command prompt or terminal.
3. Navigate to the directory where the code is located.
4. Run the following command:

```
python main.py
```

5. The server will start running on port 8008.
6. Open a web browser and visit [http://localhost:8008](http://localhost:8008).
7. The page will display the current time in Moscow.

### Notes

- The server uses the `datetime` module to get the current time.
- The server responds with a simple HTML page displaying the current time in Moscow.
- The server runs indefinitely until it is manually stopped.

### Unit Tests

In the unit tests, I have created a test case class called ```TestTimeServer``` that subclasses from ```unittest.TestCase```. This class contains two test methods:
- ```test_time_server_conntection```: This method tests the connection to the time server by sending a GET request to the server's URL. If the connection is successful, the response status code should be ```200```.
- ```test_time_servertime```: This method tests the time returned by the time server. It first gets the current UTC+3 time. Then it sends a GET request to the time server and checks if the returned time is equal to the expected time (current UTC+3 time).

To ensure that the time server is running during the tests, I have implemented the ```setUpClass``` and ```tearDownClass``` class methods. The ```setUpClass``` method starts a separate thread that runs the time server, and the ```tearDownClass``` method shuts down the server and joins the thread.

As for best practices, I have followed the following guidelines:
- I have used meaningful method and variable names to make the code easier to understand and maintain.
- I have used assertions to check the expected outcomes of the tests.
- I have handled exceptions that may occur during the tests and provided appropriate error messages.
- I have used the ```@classmethod``` decorator to denote class methods that are used for test setup and teardown.


### CI desciprion

- Name: ```CI```
- Triggers: 
  - On push to the ```main``` or ```lab3``` branches
  - On pull requests targeting the ```main``` branch
- Jobs:
  - build: Runs on the latest version of ```Ubuntu```
    - Steps:
      1. Checkout code using the ```actions/checkout``` action.
      2. Set up Python with the specified version using the ```actions/setup-python``` action with cache.
      3. Install dependencies by running ```pip install -r requirements```.txt in the app_python directory.
      4. Install the Snyk CLI globally using ```npm install -g snyk```.
      5. Authenticate Snyk by setting the API token.
      6. Run Snyk to check for vulnerabilities in all projects with a severity threshold of "high".
      7. Run the flake8 linter for Python code.
      8. Run unit tests using ```python3 -m unittest discover``` in the app_python directory.
      9. Fix Snyk vulnerabilities using the Snyk wizard.
      10. Login to Docker Hub using the ```docker/login-action``` action and the specified username and password.
      11. Build and push a Docker image using the ```docker/build-push-action``` action with the specified context, push flag, and tags.


#### Feel free to contact me if you have any questions:

Email: [e.shalagin@innopolis.university](mailto:e.shalagin@innopolis.university)

Telegram: [@Shalagin_Egor](https://t.me/Shalagin_Egor)