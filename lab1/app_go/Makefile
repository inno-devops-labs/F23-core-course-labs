.PHONY: build test clean lint

build:
	go build -o goapp

test:
	go test ./...

lint:
	go vet ./...

clean:
	rm -f goapp
