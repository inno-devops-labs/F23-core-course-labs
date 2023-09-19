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

In the unit tests, I have created a test case class called "TestTimeServer" that subclasses from unittest.TestCase. This class contains two test methods:
- testtimeserverconntection: This method tests the connection to the time server by sending a GET request to the server's URL. If the connection is successful, the response status code should be 200.
- testtimeservertime: This method tests the time returned by the time server. It first gets the current UTC time and adds 3 hours to it. Then it sends a GET request to the time server and checks if the returned time is equal to the expected time (current UTC time plus 3 hours).

To ensure that the time server is running during the tests, I have implemented the setUpClass and tearDownClass class methods. The setUpClass method starts a separate thread that runs the time server, and the tearDownClass method shuts down the server and joins the thread.

As for best practices, I have followed the following guidelines:
- I have used meaningful method and variable names to make the code easier to understand and maintain.
- I have used assertions to check the expected outcomes of the tests.
- I have handled exceptions that may occur during the tests and provided appropriate error messages.
- I have used the @classmethod decorator to denote class methods that are used for test setup and teardown.
- I have commented the code to explain the purpose and functionality of each section.


### CI desciprion

This workflow is triggered on both push events to the main and lab3 branches, as well as pull request events on the main branch. It performs the following steps:

1. Checks out the code from the repository.
2. Sets up Python 3.10.12 as the Python version.
3. Installs the project dependencies specified in the requirements.txt file.
4. Runs the Flake8 linter to check for code style and formatting issues.
5. Runs the unit tests using the unittest module.
6. Logs in to Docker Hub using the provided Docker Hub username and password.
7. Builds and pushes the Docker image using the Dockerfile located in the app_python/ directory.
8. Tags the Docker image with the specified tag name.

To use this workflow, you need to replace your-docker-hub-username with your Docker Hub username and tagname with the desired tag name for your Docker image.

Additionally, you need to create two secrets in your GitHub repository settings: DOCKER_USERNAME and DOCKER_PASSWORD. Set these secrets to your Docker Hub username and password or access token.

Commit and push these changes to your repository, and the workflow will be triggered automatically whenever there are new commits pushed to the specified branches or pull requests on the main branch.

#### Feel free to contact me if you have any questions:

Email: [e.shalagin@innopolis.university](mailto:e.shalagin@innopolis.university)

Telegram: [@Shalagin_Egor](https://t.me/Shalagin_Egor)