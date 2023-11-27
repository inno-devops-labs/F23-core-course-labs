# Web Application 

The application displays the current date and time, as this is the first lab assignment for the DevOps course at the university

## Installation

Clone the repository:

```
$ git clone https://github.com/NodirBobiev/devops-labs
$ cd devops-labs/app_go
```

## Running the Application

To start the server, navigate to the `app_go/cmd` directory and run:

```
$ export APP_GO_PORT=8081
$ go run main.go
```

The application should now be running at http://localhost:8081.

## Running the Tests

To run the tests, switch to the `app_go` directory, and execute:

```
$ go test ./..
```


## Contacts

* email: `n.bobiev@innopolis.university`
