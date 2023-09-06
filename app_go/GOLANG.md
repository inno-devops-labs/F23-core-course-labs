## Framework choice

The Gin framework is a good choice for serving a simple web application that performs web redirects due to several reasons

1. Go's Concurrency Model: Being built on Go, Gin inherits the language's robust concurrency model. 
2. Lightweight and Fast: Gin is built on top of the Go programming language, known for its speed and efficiency. Gin is designed to be lightweight and fast, making it ideal for applications that require quick response times, such as web redirects. It has minimal overhead, allowing for high-performance routing and handling of HTTP requests.

## Applied practices

- The following coding practices were implemented:
    - Test-Driven Development: unit test which verifies correctness of our returned time was implemented before the route itself. Pytest framework was used for testing. 
        - In order to ensure that the server has performed the correct redirect, we verify the response status code and the returned contents to contain URL 
    - Modularization: 
        - Utility functions like `GetEnv` which retrieves environmental variable are separated to the package `utils`
        - Controllers are separated to the page `routes` and aggregated in the `routes.go` file

