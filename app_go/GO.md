# Bonus Web Application in Golang

## Application Description

The bonus web application in Golang is designed to display the current time in Moscow. When accessing the root URL (http://localhost:8080/), the application returns the current Moscow time in the format "2006-01-02 15:04:05," including both date and time.

## Development

This application was developed using the Golang programming language and relies on the standard net/http library. The key development steps include:

- Creating an HTTP server that listens on port 8080.
- Handling requests to the root URL ("/") using an anonymous function.
- Retrieving the current time in Moscow using the time library and setting it in the HTTP response.

The application adheres to best practices and coding standards for Golang.

## Language Choice

Golang was chosen for this task for several reasons:

- **Simplicity and Performance:** Golang offers a straightforward and efficient way to create web applications, providing high performance and efficient resource utilization.

- **Standard Library:** Golang's standard library includes numerous useful tools for web application development, including support for HTTP servers and time handling.

# Running and Testing

To run the application and perform testing, follow these steps:

1. Make sure you have Golang installed. If not, [install it](https://golang.org/doc/install).

2. Copy the application code into a file with a ".go" extension, for example, "main.go."

3. Open your terminal and navigate to the directory containing your ".go" file.

4. Start the application by executing the following command:

   ```bash
   go run main.go

5. Open a web browser and go to http://localhost:8080/ to confirm that the application displays the current Moscow time.

To test the application, create a test file (e.g., "main_test.go") and include the test code as described in the previous response.

1. Run the tests using the following command:

    ```bash
    go test
   
After completing these steps, you should observe that your application is running and passing the tests successfully.

# Unit Tests

In this Go application, I have implemented comprehensive unit tests to ensure the correctness of the code. Here are the unit tests that have been created:

## `TestMainHandler`

This test checks the `mainHandler` function, which handles HTTP requests to the root URL ("/"). It verifies the following:
- The response status code is 200 OK.
- The response body contains the current Moscow time in the correct format.

## `TestServer`

This test starts a test HTTP server using `httptest.NewServer` and sends a GET request to it. It verifies the following:
- The response status code is 200 OK.
- The response body contains the current Moscow time in the correct format.

## `TestMain`

This test is for the `main` function. It doesn't directly test the HTTP server but ensures that the `main` function doesn't cause any panics or errors. It starts the `main` function in a goroutine and waits for a short time to allow the server to start.

To run these tests, you can use the `go test` command.


