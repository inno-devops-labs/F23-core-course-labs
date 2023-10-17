package main

import (
	"app_go/handler"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler.IndexHandler)
	err := http.ListenAndServe(":8081", nil)
	handler.Error(err)
}
