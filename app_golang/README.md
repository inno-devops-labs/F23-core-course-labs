# Golang Web Application

This is a simple Golang web application that displays the current time in Moscow.

## Prerequisites

Before running this application, make sure you have Go installed on your machine.

## Usage

To run the application, use the following command:

```go run main.go```

The application will start running on http://localhost:8008.

## Example Response

When you access the http://localhost:8008, you will see a response like this:

Current time in Moscow: 2022-01-19T20:30:00Z


## Dependencies

This application uses the following dependencies:

- net/http: This package is used for creating HTTP servers and handling HTTP requests.
- time: This package is used for handling time and timezones.
