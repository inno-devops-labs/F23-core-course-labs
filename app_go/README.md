# Web Application 

[![Go App](https://github.com/NodirBobiev/devops-labs/actions/workflows/app_go.yaml/badge.svg)](https://github.com/NodirBobiev/devops-labs/actions/workflows/app_go.yaml)

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
$ go test .
```

## Docker 
To build the image run the following command from `app_go` directory:
```
docker build -t devopsgo .
```

To run the image run:
```
docker run --rm -p 8080:8080 devopsgo
```

* `--rm` here stands for deleting the container right after it is stopped

Or if you want to pull the image from the docker hub:


```
docker pull bobievnodir/devopsgo:v1.0
```


## Contacts

* email: `n.bobiev@innopolis.university`
