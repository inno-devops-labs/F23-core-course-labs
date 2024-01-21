# Unit Tests for Flask Application

The Flask application's functionality is tested using a set of unit tests. Here's a breakdown of these tests and the best practices followed:

## Best Practices:

1. **Setup and Teardown**: Use `setUp` method to initialize testing environment and resources before each test. This ensures each test runs in a controlled and consistent environment.
2. **Test Independence**: Each test function is independent and verifies a specific functionality or behavior. Tests do not rely on the success of others.
3. **Descriptive Test Names**: Test function names are descriptive enough to understand the functionality being tested.
4. **Assert Functions**: Use appropriate `assert` methods to compare the expected outcome to the actual result.

## Tests:

### 1. `test_moscow_time_format`

- **Purpose**: This test verifies that the `get_moscow_time` function returns Moscow time in the correct format.
- **Implementation**:
  - The function's return value is checked to ensure it matches the expected date-time format. 
  - A successful conversion to a datetime object confirms that the format is correct.

### 2. `test_moscow_time_endpoint`

- **Purpose**: To test the main endpoint of the application which displays Moscow time.
- **Implementation**:
  - A GET request is made to the root endpoint.
  - The test ensures that the server returns a 200 OK status.
  - The response's content is checked for the presence of "Current Moscow Time".

### 3. `test_healthcheck_endpoint`

- **Purpose**: To test the health check endpoint of the application.
- **Implementation**:
  - A GET request is made to the `/health` endpoint.
  - The test ensures that the server returns a 200 OK status.
  - The response's content is checked to ensure the application is healthy.
  