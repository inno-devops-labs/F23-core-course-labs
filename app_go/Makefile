.PHONY: build test clean

image_name ?= ar7ch/devops-app-go

build:
	go build -o goapp

test:
	go test ./...

unit-tests: test

clean:
	rm -f goapp

.PHONY: lint test docker docker-build docker-lint docker-check

tag ?= latest

docker:
	docker build -t $(image_name):$(tag) .

docker-build: docker

docker-pull:
	docker pull $(image_name):latest

docker-run:
	docker run -it -p 8080:80 $(image_name):$(tag)

docker-push:
	docker push $(image_name):$(tag)

docker-check:
	docker scout quickview $(image_name):$(tag)

docker-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
