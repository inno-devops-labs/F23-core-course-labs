I've decided to take a test-driven approach so I've written tests before implementing certain functionality in the application. Tests are carried out using Go's builtin `go test` functionality.
Since my app consists of only API endpoint that shows time, I've created unit test that checks if the endpoint returns correct time. I've also created a simple integration test that checks if the app is running and returns correct time.

Best practices in testing I've implemented:
* Unit tests are isolated from each other
* Unit tests are isolated from external dependencies
* Follow AAA pattern in unit tests is followed
* Besides unit tests, I've created component and system (integration) tests that check if the app server is running and returns correct time

