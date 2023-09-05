## Framework
I didn't use any framework, because standard "net/http" Go package is enough.

## Best practices
1. Files are separated by their types (server endpoints, page templates, entities and config are separated). Such structure is easier to expand and easier to navigate.
2. Using env file. It's a common web server security practise

## Coding standards and testing
1. I use standard `goimports` and `gofmt` commands to ensure code standards.
2. I've faced some problems while writing unit tests for endpoints, so here I just used manual testing.