## Framework
I didn't use any framework, because standard "net/http" Go package is enough.

## Best practices
1. Files are separated by their types (server endpoints, page templates, entities and config are separated). Such structure is easier to expand and easier to navigate.
2. Using env file. It's a common web server security practise

## Coding standards and testing
1. I use standard `goimports` and `gofmt` commands to ensure code standards.
2. You can run unit tests using `go test -v` command

## Unit tests
I've implemented 2 unit tests for root and joke handlers, these tests cover all functionality (fetching jokes, generating html page).
Best practices that I've followed:
* Using httptest test client to test responses.
* Test edge cases, using positive and negative tests
* Tests are independent and do not rely on each other