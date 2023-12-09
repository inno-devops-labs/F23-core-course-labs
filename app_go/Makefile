.PHONY: build test clean

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
	docker build -t beleet/devops_lab3_app_go:$(tag) .

docker-build: docker

docker-pull:
	docker pull beleet/devops_lab3_app_go:latest

docker-run:
	docker run -it -p 8080:80 beleet/devops_lab3_app_go:$(tag)

docker-push:
	docker push beleet/devops_lab3_app_go:$(tag)

docker-check:
	docker scout quickview beleet/devops_lab3_app_go:$(tag)

docker-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
