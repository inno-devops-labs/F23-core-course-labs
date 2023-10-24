package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	timeHandlerProcessed = promauto.NewCounter(prometheus.CounterOpts{
		Name: "time_handler_processed",
		Help: "The total number of time handler calls",
	})
)

const timeFormat = "2006-01-02 15:04:05"

func currentMoscowTimeHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("GET TIME / HTTP")

	timeHandlerProcessed.Inc()

	location, err := time.LoadLocation("Europe/Moscow")
	if err != nil {
		log.Println(err)
		http.Error(w, "Internal server error", http.StatusInternalServerError)
	}

	currentTime := time.Now().In(location)
	fmt.Fprint(w, currentTime.Format(timeFormat))
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("GET HEALTH / HTTP")

	w.WriteHeader(http.StatusOK)
	fmt.Fprint(w, "Server is healthy")
}

func main() {
	http.Handle("/metrics", promhttp.Handler())
	http.HandleFunc("/health", healthHandler)
	http.HandleFunc("/", currentMoscowTimeHandler)
	if err := http.ListenAndServe(":9000", nil); err != nil {
		log.Fatal(err)
	}
}
