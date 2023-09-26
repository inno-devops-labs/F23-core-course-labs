# Go web application

## Overview

This is a simple web application that shows the current exchange rate of cryptocurrencies (BTC, ETH, DOGE and SOL) to USD.

## Requirements

To run the application, you need a Golang version of 1.20. [How to install Golang](https://go.dev/doc/install)


## Docker

You can run this application in docker container.

Build image inside app_go directory:

```bash
docker build -t rakavaqaflow/app-go:v1 .
```

Or

Pull image from DockerHub:
```bash
docker pull rakavaqaflow/app-go:v1
```

And run docker image:

```bash
docker run -p 9000:9000 rakavaqaflow/app-go:v1
```


## Run

To run app you need run the command inside app_go folder:
```bash
go run cmd/main.go
```

## Usage

To see the result of the work, open a browser and go to http://localhost:9000/ - you will see current exchange rate of cryptocurrencies (BTC, ETH, DOGE and SOL) to USD.

## Contact

email: v.khalilov@innopolis.university
tg: @vaqaaa 
