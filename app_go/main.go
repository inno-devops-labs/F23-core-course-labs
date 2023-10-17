package main

import (
	"app_go/config"
	"app_go/routes"
	"log"
	"net/http"
)

func main() {
	cfg := config.NewConfig()
	mux := http.NewServeMux()

	mux.HandleFunc("/", routes.MainHandler)
	mux.HandleFunc("/joke", routes.JokeHandler)
	log.Print("App started")
	err := http.ListenAndServe(cfg.ServerHost+":"+cfg.ServerPort, mux)

	if err != nil {
		return
	}
}
