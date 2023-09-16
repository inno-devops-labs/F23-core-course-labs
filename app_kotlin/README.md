# Base converter
App for converting any number in base 10 into any base

## Run

```bash
./gradlew bootRun
```
App will start at default 8080 port.
To change port, go to application.yaml file

## Test
```bash
./gradlew test
```

## Docker
To build docker image:
```bash
docker build --tag edikgoose/base-converter:1.0.0 .
```

To pull docker image:
```bash
docker pull edikgoose/base-converter:1.0.0 
```

To run docker image:
```bash
docker run -p 8080:8080 --name base-converter edikgoose/base-converter:1.0.0
```

## Contributing
Project are open to contributing, any forks are welcome.

## Authors and acknowledgment
Eduard Zaripov - e.zaripov@innopolis.university
