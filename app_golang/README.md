# Moscow Time
- Simple app that shows the current time in MSK Timezone.

## Used technology
- GoLang

## Development

`golang` is used, make sure you have it installed then execute the following:

```bash
go mod download # although not necessary, because there are no external dependencies
go run main.go # you can access the website on http://localhost:8080/
```

## Testing

```bash
go test
```

## Docker
This full application has been uploaded to [dockerhub](https://hub.docker.com/r/iviosab/moscow_time_go), you can fully test it by either pulling the image from dockerhub or building the Dockerfile in this directory and then running it. 
#### Build 
```bash
# make sure you are in the app_python directory
docker build -t <name> .
```
#### Pull
```bash
docker pull iviosab/moscow_time_go
```
#### Run
```bash
docker run --rm -p 8080:8080 iviosab/moscow_time_go
```