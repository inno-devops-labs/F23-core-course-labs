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


## Endpoints description

### Endpoint: /
* Description: This endpoint increments a counter each time it is called and returns the current time in Moscow. It also writes the current counter value to a file named 'visits'.
* HTTP Method: GET
* Response: A string containing the current time in Moscow and the number of times the endpoint has been called.


### Endpoint: /healthcheck
* Description: This endpoint returns a simple "OK" message. It is used for health checks to verify that the server is running.
* HTTP Method: GET
* Response: A string "OK".


### Endpoint: /metrics
* Description: This endpoint returns the current metrics of the server. It uses the Prometheus client library to generate the metrics.
* HTTP Method: GET
* Response: A string containing the current metrics of the server.


### Endpoint: /visits
* Description: This endpoint returns the current counter value. The counter is incremented each time the root endpoint (/) is called.
* HTTP Method: GET
* Response: A string containing the current counter value.