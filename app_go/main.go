package main

import (
	"app_go/config"
	"app_go/routes"
	"log"
	"net/http"

	"github.com/gorilla/mux"

	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	cfg := config.NewConfig()
	r := mux.NewRouter()

	r.Path("/metrics").Handler(promhttp.Handler())

	r.HandleFunc("/health", routes.HealthHandler)
	r.HandleFunc("/", routes.MainHandler).Methods("GET")
	r.HandleFunc("/joke", routes.JokeHandler).Methods("GET")

	log.Print("App started")
	srv := http.Server{
		Addr:    cfg.ServerHost + ":" + cfg.ServerPort,
		Handler: r,
	}
	err := srv.ListenAndServe()
	if err != nil {
		return
	}

	if err != nil {
		return
	}
}
