package controller

import (
	"log"
	"net/http"
	"sync"
	"sync/atomic"
	"time"

	"github.com/gorilla/mux"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

func Router(buildTime, commit, release string) *mux.Router {
	isReady := &atomic.Value{}
	isReady.Store(false)
	m := sync.Mutex{}

	go func() {
		log.Println("Readyz probe is negative by default")
		time.Sleep(1 * time.Second) // For warming up the cache
		isReady.Store(true)
		log.Println("Readyz probe is positive")
	}()

	r := mux.NewRouter()

	// Prometheus metrics
	r.Path("/metrics").Handler(promhttp.Handler())

	subrouter := r.Methods("GET").Subrouter()
	subrouter.HandleFunc("/home", ApplyMiddleware(
		home(buildTime, commit, release),
		addVisitsCounter(&m),
	).ServeHTTP)

	r.HandleFunc("/visits", visits)

	r.HandleFunc("/healthz", healthz)
	r.HandleFunc("/readyz", readyz(isReady))
	return r
}

func ApplyMiddleware(handler http.Handler, middlewares ...mux.MiddlewareFunc) http.Handler {
	for i := range middlewares {
		handler = middlewares[i](handler)
	}

	return handler
}