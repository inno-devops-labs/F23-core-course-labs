[![Go Workflow](https://github.com/vladislav5ik/core-course-labs/actions/workflows/golang.yml/badge.svg)](https://github.com/vladislav5ik/core-course-labs/actions/workflows/golang.yml)
# Time-app

Time-app is a Go web application that displays the current time in Moscow.

## Installation using docker
### Build docker image
To build the Docker image, clone the repo, and use the following command inside `app_go` directory:
```
docker build --tag timeapp-go .
```
### Run docker container
To run the Docker container after building it, use the following command:
```
docker run -p 8080:8080 timeapp-go:latest
```
### Pull docker image
To pull an image from a Docker registry, use the following command:
```
docker pull vladspigin/timeapp-go:latest
```

### Run
Make sure Golang is installed before running app. No additional packages are required.
```
go run timeapp.go
```
Now you can open `http://127.0.0.1:3000/` in your browser to check the time. Also you can specify another port using enviromental vriable `APP_PORT`.
```
APP_PORT=7777 go run timeapp.go
```

### Development

Install pre-commit to automatically lint files.

### Unit Tests
Run tests:
```
go test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
