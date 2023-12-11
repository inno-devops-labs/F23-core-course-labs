package main

import (
	"app_go/internals/handlers"
	"app_go/internals/middlewares"
	"log"
	"net/http"
	"os"

	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	port := os.Getenv("APP_GO_PORT")
	if port == "" {
		port = "8080"
	}
	addr := ":" + port
	http.Handle("/metrics", promhttp.Handler())
	http.Handle("/", middlewares.PrometheusMetrics(handlers.NewTimeHandler()))

	log.Printf("Server is starting on port %s...", port)

	if err := http.ListenAndServe(addr, nil); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}

}
