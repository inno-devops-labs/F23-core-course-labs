# Web service

## Framework

I've chosen Gorilla mux because its 1 of the most useful frameworks for Go to create web application.

1. **Powerful routing**: Gorilla Mux offers a powerful and flexible router that allows you to define complex URL patterns.
2. **Middleware Support**: It supports middleware, enabling you to add logic to request/response handling process.
3. **Performance**: Gorilla Mux leverages performance of Golang by providing efficient routing and handling HTTP requests.
4. **Compatibility**: Gorilla Mux integrates seamlessly with the standard `net/http` package in Go, making it easy to write code.
5. **Testing**: By integration with `net/http` package Gorilla Mux provides easy testing by using `net/http/httptest` package.
It allows you to write *unit* and *integration* tests.

## Best practises

1. **Logging**: All handlers are covered by logs.
1. **Tests**: All routes are covered by tests using `net/http/httptest` package that allows you to easily write tests for web application.
1. **Configuration by environment variables**: Port and app name are configured by environment variables.
So, you can change some settings without changing the code.
1. **Versioning**: The application has version that allows you to control release time.
It also has commit time and build time that allows you to find difference between old and new versions of the application 
and to check when the application was ready for release.
1. **Makefile**: You can easily build and run the application using simple command provided by `Makefile`.