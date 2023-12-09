.PHONY: lint test docker docker-build docker-lint docker-check

tag ?= latest

lint:
	flake8 ./app

test:
	cd ./app && python3 -m pytest

unit-tests:
	cd ./app && python3 -m pytest tests/unit

docker:
	@echo "=== Building Docker image verion $(tag)"
	docker build -t beleet/devops_lab3_app_python:$(tag) .
	@echo "=== Build Docker image verion $(tag) done"

docker-build: docker

docker-pull:
	docker pull beleet/devops_lab3_app_python:latest

docker-run:
	docker run -it -p 8080:80 beleet/devops_lab3_app_python:$(tag)

docker-push:
	docker push beleet/devops_lab3_app_python:$(tag)

docker-check:
	docker scout quickview beleet/devops_lab3_app_python:$(tag)

docker-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
