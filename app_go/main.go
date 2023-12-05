package main

import (
	"app_go/config"
	"app_go/routes"
	"log"
	"net/http"
	"os"

	"github.com/gorilla/mux"

	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var CounterFilePath = "./data/visits.json"

func main() {
	cfg := config.NewConfig()
	r := mux.NewRouter()

	r.Path("/metrics").Handler(promhttp.Handler())

	r.HandleFunc("/health", routes.HealthHandler)
	r.HandleFunc("/", routes.MainHandler).Methods("GET")
	r.HandleFunc("/joke", routes.JokeHandler).Methods("GET")
	r.HandleFunc("/visits", routes.VisitsHandler).Methods("GET")

	_, err := os.Stat(CounterFilePath)
	if err != nil {
		f, err := os.Create(CounterFilePath)
		if err != nil {
			log.Fatal(err)
		}

		_, err = f.Write([]byte(`{"visits":"0"}`))
		err = f.Close()
		if err != nil {
			log.Fatal(err)
		}
	}

	log.Print("App started")
	srv := http.Server{
		Addr:    cfg.ServerHost + ":" + cfg.ServerPort,
		Handler: r,
	}
	err = srv.ListenAndServe()
	if err != nil {
		return
	}

	if err != nil {
		return
	}
}
