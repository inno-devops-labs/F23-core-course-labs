package main

import (
	"app_go/handler"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler.IndexHandler)
	err := http.ListenAndServe(":3000", nil)
	handler.Error(err)
}
