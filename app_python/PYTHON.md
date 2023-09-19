# Python Web Application 

> This is a python app that displays a current time in Moscow, it implements best practices and follows coding standarts. It was tested and the time updates upon page refreshing.

## Framework choice

> For this task I choose to use Flask as a framework. 

**Flask is a good framework for this task because:**

1. `Simplicity` : 
    - It is minimalistic and doesn't come with unnecessary features. For a small application like this, simplicity is an advantage. 

2. `Flexibility` : 
    - There is no rigid structure, that allows me to organize the project as I see fit, More precisely I was able to use `html`, and did not have the need to learn any custom markup language instead.

## Best practices 

1. `PEP 8`:
    - I followed PEP 8 guidelines.

2. `Zen of Python`:
    - In order to uphold best practices I followed 'Zen of Python'


## Coding standards 

> PEP 8 coding standads were used. Below the description of some coding standards that I used.

1. `Tabs or spaces`: 
    - I used spaces as it it a preferred indentation method. 

2. `Maximum Line Length`: 
    - My maximum line length did not exceed 79 characters.

3. `Imports`:
    - Import are on separate lines.

4. `Whitespace in expressions and statements`: 
    - All extraneous whitespace are avoided.

# Unit Tests for Flask Application

This document describes the unit tests for the Flask application that generates and displays the current time in the 'Europe/Moscow' timezone.

## Test Coverage

The unit tests cover the following aspects of the Flask application:

1. **HTTP Status Code**: The test checks if the HTTP status code of the response is 200, indicating a successful response.

2. **Template Usage**: The test ensures that the 'time.html' template is used for rendering the response. The response is taken, and the absolute difference between displayed time and actual time is checked. In case if it is higher than 5 seconds, the exceptions is thrown. 

You can extend the test suite to cover additional aspects of the application, such as checking the time format, verifying the correct timezone, or testing edge cases.

## Unit Testing Best Practices

 1. Isolation of Tests
    - Each test method (`test_display_time_status_code` and `test_display_time_difference`) focuses on testing a specific aspect of the application's functionality. This ensures that each test is isolated and independent, making it easier to pinpoint issues when failures occur.

 2. Test Setup with `setUp`
    - The `setUp` method is utilized to set up any common resources or configurations needed for the tests. In this case, it initializes a test client for the Flask application, ensuring that the client is available for all test methods.
        ```python
        def setUp(self):
            self.app = app.test_client()
        ```

 3. Clear and Descriptive Test Method Names 
    - The test method names are clear and descriptive, indicating what aspect of the application's functionality is being tested. For example, test_display_time_status_code tests the HTTP status code, and test_display_time_difference tests the time difference calculation

 4. Assertions for Expected Outcomes 
    - The unittest library's assert methods are used to make assertions about expected outcomes. For instance, self.assertEqual(response.status_code, 200) checks if the HTTP status code is 200, indicating a successful response.

 5. Printing Informative Messages
    - Informative messages are printed to the console upon test success or failure. For example, the absolute time difference is printed for the test_display_time_difference test.
    ```python 
    print("\nThe absolute time difference is : " + str(abs(time_difference)))
    ```
 6. Main Guard for Test Execution 
    - The if ```__name__ == '__main__'```: block ensures that the tests are executed when the script is run directly. This allows running the tests without the need for external test runners.
    ```python 
    if __name__ == '__main__':
    unittest.main()
    ```

## Running the Unit Tests

To run the unit tests, follow these steps:

1. Ensure that you have the necessary Python packages installed. You can use `pip` to install them if needed:

```bash
pip install Flask unittest
```

2. Run the test script. 

```bash 
python test_app.py
```

