PROJECT?=github.com/YeslieSnayder/devops-course-labs/app_golang

RELEASE?=0.0.1
COMMIT?=$(shell git rev-parse --short HEAD)
BUILD_TIME?=$(shell date -u '+%Y-%m-%d_%H:%M:%S')

APP?=app
PORT?=8000

clean:
	rm -f ${APP}

build: clean
	go build \
			-ldflags "-s -w -X ${PROJECT}/version.Release=${RELEASE} \
			-X ${PROJECT}/version.Commit=${COMMIT} -X ${PROJECT}/version.BuildTime=${BUILD_TIME}" \
			-o ${APP}

run: build
	PORT=${PORT} ./${APP}

test:
	go test -v -race ./...