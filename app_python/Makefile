.PHONY: lint test docker docker-build docker-lint docker-check

tag ?= latest
image_name ?= ar7ch/devops-app-python

lint:
	flake8 ./app

test:
	cd ./app && python3 -m pytest

unit-tests:
	cd ./app && python3 -m pytest tests/unit

docker:
	@echo "=== Building Docker image $(image_name) version $(tag)"
	docker build -t $(image_name):$(tag) .
	@echo "=== Build Docker image $(image_name) version $(tag) done"

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
