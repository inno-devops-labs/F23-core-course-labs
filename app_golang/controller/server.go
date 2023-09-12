package controller

import (
	"log"
	"sync/atomic"
	"time"

	"github.com/gorilla/mux"
)

func Router(buildTime, commit, release string) *mux.Router {
	isReady := &atomic.Value{}
	isReady.Store(false)

	go func() {
		log.Println("Readyz probe is negative by default")
		time.Sleep(1 * time.Second) // For warming up the cache
		isReady.Store(true)
		log.Println("Readyz probe is positive")
	}()

	r := mux.NewRouter()
	r.HandleFunc("/home", home(buildTime, commit, release)).Methods("GET")
	r.HandleFunc("/healthz", healthz)
	r.HandleFunc("/readyz", readyz(isReady))
	return r
}
